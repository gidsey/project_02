"""Create three equal ability soccer teams from a supplied list of players."""
import csv


if __name__ == "__main__":

    players = {}
    exp_players = []
    ama_players = []
    all_players = []
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
            all_players.append(player_info)
            if (item[1][0]) == 'YES':
                exp_players.append(player_info)
            else:
                ama_players.append(player_info)

        # Assign an equal number of experienced & amateur players to each team
        for player in exp_players:
            sharks.append(exp_players.pop())
            sharks.append(ama_players.pop())
            raptors.append(exp_players.pop())
            raptors.append(ama_players.pop())
            dragons.append(exp_players.pop())
            dragons.append(ama_players.pop())

        return all_players

    def write_list():
        """Write out the text files."""
        formatting = '\n' + "=" * 8 + '\n'
        with open("teams.txt", "w") as file:
            file.write("\nSharks" + formatting)
            for line in sharks:
                file.write(line + '\n')
            file.write("\nRaptors" + formatting)
            for line in raptors:
                file.write(line + '\n')
            file.write("\nDragons" + formatting)
            for line in dragons:
                file.write(line + '\n')

    def make_welcome_letters():
        """Create the individual welcome letters."""
        for item in players.items():
            guardian = item[1][1]
            player = item[0]
            # Use of .replace()
            # Ref: https://tinyurl.com/yxhxwrhk
            file_name = player.replace(' ', '_')
            # Get the player's team
            # Check if a sublist contains an item
            # Ref: https://tinyurl.com/y4njcjr9
            if any(player in i for i in sharks):
                thisteam = "SHARKS"
            elif any(player in i for i in raptors):
                thisteam = "RAPTORS"
            elif any(player in i for i in dragons):
                thisteam = "DRAGONS"
            line1 = 'Dear {}, '.format(guardian)
            line2 = 'We are pleased to tell you that {} has been chosen to play in the {}!'.format(player, thisteam)
            line3 = 'The next practice day is on Sunday at 11am sharp.'
            line4 = 'Looking forward to seeing you there.'
            line5 = 'Love from the Python team x'
            # Use of writelines()
            # Ref: https://tinyurl.com/yyjvd692
            with open(file_name.lower() + ".txt", "w") as file:
                file.writelines('\n\n'.join([line1, line2, line3, line4, line5]))

    get_players('soccer_players.csv')
    make_teams()
    write_list()
    make_welcome_letters()
