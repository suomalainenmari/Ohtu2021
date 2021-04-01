HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
      if summa>=0:
        kortti.lataa(summa)
        return True
      else:
        return False

    def osta_lounas(self, kortti):
      if kortti.saldo<5:
        return False
      else:
          kortti.osta(HINTA)
          self.myytyja_lounaita = self.myytyja_lounaita + 1
          return True
