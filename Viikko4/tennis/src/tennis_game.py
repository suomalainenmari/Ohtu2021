class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_names = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def game_is_tie(self):
      if self.m_score1 <4:
        return f"{self.score_names[self.m_score1]}-All"
      else:
        return "Deuce"

    def game_is_not_tie(self):
      if self.m_score1<4 and self.m_score2<4:
        return f"{self.score_names[self.m_score1]}-{self.score_names[self.m_score2]}"
      else:
        if self.m_score1-self.m_score2==1:
          return "Advantage player1"
        elif self.m_score1-self.m_score2>=2:
          return "Win for player1"
        elif self.m_score2-self.m_score1>=2:
          return "Win for player2"
        else:
          return "Advantage player2"
        

    def get_score(self):
        score = ""
        if self.m_score1 == self.m_score2:
          score=self.game_is_tie()
        
        else:
          score=self.game_is_not_tie()

        return score
