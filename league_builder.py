"""Create three equal ability soccer teams from a supplied list of players."""
import csv


if __name__ == "__main__":

    players = {}

    with open('soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        rows = list(player_reader)
        for row in rows:
            # print(row)
            players[row['Name']] = \
             [row['Soccer Experience'], row['Guardian Name(s)']]
        print("\nplayers: {}\n".format(players))
