class Player():
    #player class so multiple people can play and keep track of points, games won, etc
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.games_won = 0
        self.games_lost = 0
        self.highest_scoring_word = ''
        self.best_game = ''
    def increment_points(self, increment):
        pass
list_of_players = []
#need record of players so can't have multiple players with same name
def player_menu():
    #prompts user to create or load a player
    choice = input("Would you like to create a new player or load an existing one?\nCreate\nLoad\n")
    if choice.lower() == 'create':
        create_player()
    elif choice.lower() == 'load':
        load_player()
    else:
        print("error")

def create_player():
    #function for creating player
    while True:
        name = input("What is your name?").capitalize()
        #if there is already a character with that name, prompts user to input different name
        if name in list_of_players:
            print(f"There is already a player called {name}. Please pick a different name.")
            continue
        new_player = Player(name)
        list_of_players.append(new_player.name)
        return

def load_player():
    print(list_of_players)
    player_to_load = input("Which player are you?")
    if player_to_load not in list_of_players:
        print(f"{player_to_load} does not exist. Please create this player or load a different one.")
    else:
        return

