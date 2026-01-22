from player_class import Player

def player_menu():
    #prompts user to create or load a player
    while True:
        choice = input("\rWould you like to create a new player, load an existing one, or exit?\n•Create\n•Load\n•Exit\n")
        if choice.lower() == 'create':
            create_player()
        elif choice.lower() == 'load':
            load_player()
        elif choice.lower() == 'exit':
            return
        else:
            print("error")

def create_player():
    while True:
        player_name = input("What is the player called?\n")
        try:
            new_player = Player.create(player_name.capitalize())
            if new_player:  
                print(f"Created {player_name}!")
                return
                Player.save()
        except:
            print('error')
            continue

def load_player():
    if not Player.players:
        print("No players have been created. Please create a player first.")
        return None
    print("Available players:", ", ".join(Player.players.keys()))

#player_menu()