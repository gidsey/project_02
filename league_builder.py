"""Create three equal ability soccer teams from a supplied list of players."""
import csv


if __name__ == "__main__":

    experienced_players = {}
    with open('soccer_players.csv', newline='') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        rows = list(player_reader)
        for row in rows:
            # print(row)
            print("name = {} / experience = {}".format(row['Name'], row['Soccer Experience']))


