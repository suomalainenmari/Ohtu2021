from player import Player
from playerstats import PlayerStats
from playerreader import PlayerReader


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    for player in players:
      print(player)



if __name__ == "__main__":
    main()