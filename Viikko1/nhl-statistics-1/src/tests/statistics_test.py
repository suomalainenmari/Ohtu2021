import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_konstruktori_luo_statistiikat(self):
      edmonton = self.statistics.team("EDM")
      sizeofedmonton = len(edmonton)
      self.assertAlmostEqual(sizeofedmonton, 3)

    def test_search_palauttaa_pelaajat(self):
      self.assertAlmostEqual(str(self.statistics.search("Kurri")), "Kurri EDM 37 + 53 = 90")

    def test_search_palauttaa_None_jos_ei_pelaajaa_loydy(self):
      self.assertAlmostEqual(str(self.statistics.search("Mari")), "None")

    def test_sort_by_points_palauttaako(self):
      pistemiehet = self.statistics.top_scorers(4)
      self.assertAlmostEqual(str(pistemiehet[1]),"Lemieux PIT 45 + 54 = 99")