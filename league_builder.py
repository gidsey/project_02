"""Create three equal ability soccer teams from a supplied list of players."""
import csv
import sys


if __name__ == "__main__":

    players = {}
    exp_players = []
    ama_players = []
    sharks = []
    raptors = []
    dragons = []

    def get_players(file):
        """Create a dictionary of players from the CSV file."""
        with open('soccer_players.csv', newline='') as csvfile:
            player_reader = csv.DictReader(csvfile, delimiter=',')
            rows = list(player_reader)
            for row in rows:
                players[row['Name']] = \
                 [row['Soccer Experience'], row['Guardian Name(s)']]
            return players


    def make_teams():
        """Assign players into mixed ability teams."""
        # Create a separate list of experineced platers and amateur players

        for item in players.items():
            player_info = ', '.join([item[0], item[1][0], item[1][1]])
            if (item[1][0]) == 'YES':
                exp_players.append(player_info)
            else:
                ama_players.append(player_info)
            # print("\nexp_players = {}\n".format(exp_players))
        # print("\nama_players = {}\n".format(ama_players))

        # Assign an equal number of exp and amateur plater to ech team
        for player in exp_players:
            sharks.append(exp_players.pop())
            raptors.append(exp_players.pop())
            dragons.append(exp_players.pop())

        for player in ama_players:
            sharks.append(ama_players.pop())
            raptors.append(ama_players.pop())
            dragons.append(ama_players.pop())


        # print("\nDragons = {}\n".format(dragons))
        # print("\nSharks = {}\n".format(sharks))
        # print("\nRaptors = {}\n".format(raptors))


    def write_List():
        """Write out the text files."""
        with open("teams.txt", "w") as file:
            file.write("\nSharks" + '\n' + "=" * 10 + '\n')
            for line in sharks:
                file.write(line + '\n')
            file.write("\nRaptors" + '\n' + "=" * 10 + '\n')
            for line in raptors:
                file.write(line + '\n')
            file.write("\nDragons" + '\n' + "=" * 10 + '\n')
            for line in dragons:
                file.write(line + '\n')


    get_players('soccer_players.csv')
    make_teams()
    write_List()
