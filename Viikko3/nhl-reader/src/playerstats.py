class PlayerStats:
  def __init__(self,reader):
    self.players = reader.get_players()

  def top_scorers_by_nationality(self,nationality):
    wantedPlayers = [] 
    for player in self.players:
      if player.nationality==nationality:
        wantedPlayers.append(player)

    wantedPlayers.sort(key=lambda x: x.goals+x.assists, reverse = True)
    return wantedPlayers