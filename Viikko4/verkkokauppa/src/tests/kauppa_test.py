import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
      self.pankki_mock = Mock()
      self.viitegeneraattori_mock = Mock()

      # palautetaan aina arvo 42
      self.viitegeneraattori_mock.uusi.return_value = 42

      self.varasto_mock = Mock()

      # tehdään toteutus saldo-metodille
      def varasto_saldo(tuote_id):
        if tuote_id == 1:
          return 10
        if tuote_id== 2:
          return 5
        if tuote_id==3:
          return 0

      # tehdään toteutus hae_tuote-metodille
      def varasto_hae_tuote(tuote_id):
        if tuote_id == 1:
          return Tuote(1, "maito", 5)
        if tuote_id==2:
          return Tuote(2,"leipä", 3)
        if tuote_id==3:
          return Tuote(3, "juusto", 4)

      # otetaan toteutukset käyttöön
      self.varasto_mock.saldo.side_effect = varasto_saldo
      self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

      # alustetaan kauppa
      self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
      # tehdään ostokset
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      self.kauppa.tilimaksu("pekka", "12345")

      # varmistetaan, että metodia tilisiirto on kutsuttu
      self.pankki_mock.tilisiirto.assert_called()
      # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kun_tuote_lisatty_kutsutaan_pankin_metodia_tilisiirto_oikeilla_tiedoilla(self):
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      self.kauppa.tilimaksu("joni","23456")
      
      self.pankki_mock.tilisiirto.assert_called_with("joni", ANY, "23456", ANY, 5)

    def test_ostosten_jalkeen_pankin_metodia_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      self.kauppa.lisaa_koriin(2)
      self.kauppa.tilimaksu("joni","34567")

      self.pankki_mock.tilisiirto.assert_called_with("joni", ANY,"34567", ANY, 8)

    def test_kun_tuote_loppu_tilisiirron_kutsun_summaan_ei_lisatty_loppuneen_tuotteen_hintaa(self):
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      self.kauppa.lisaa_koriin(3)
      self.kauppa.tilimaksu("joni", "34567")

      self.pankki_mock.tilisiirto.assert_called_with("joni", ANY, "34567", ANY, 5)

    def test_aloita_asiointi_metodin_kutsu_nollaa_ostosten_tiedot(self):
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      #aloitetaan asiointi uudestaan ja tarkistetaan kutsutaanko tilisiirtoa uuden asioinnin summalla
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(2)
      self.kauppa.tilimaksu("joni","23456")
      self.pankki_mock.tilisiirto.assert_called_with("joni",ANY,"23456",ANY,3)

    def test_kauppa_pyytaa_uuden_viitenumeron_joka_maksutapahtumalle(self):
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      self.kauppa.tilimaksu("joni","23456")

      self.assertEqual(self.viitegeneraattori_mock.uusi.call_count,1)

      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(2)
      self.kauppa.tilimaksu("joni","23456")
      self.assertEqual(self.viitegeneraattori_mock.uusi.call_count,2)

    def test_ostoskorista_poistettu_tuote_palautuu_varaston_saldoon(self):
      self.kauppa.aloita_asiointi()
      self.kauppa.lisaa_koriin(1)
      self.kauppa.poista_korista(1)

      self.assertEqual(self.varasto_mock.palauta_varastoon.call_count,1)

