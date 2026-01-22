import json

class Player():
    #player class so multiple people can play and keep track of points, games won, etc
    players = {} #class variable listing all existing players
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.games_won = 0
        self.games_lost = 0
        self.highest_scoring_word = ''
        self.best_game = ''
        Player.players[name] = self

    def increment_points(self, increment):
        pass

    @classmethod
    def load(cls):
        #load player information from data file
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for name, player_data in data.items():
                            player = cls(name)
                            player.points = player_data['points']
                            player.games_won = player_data['games won']
                            player.games_lost = player_data['games_lost']
                            player.highest_scoring_word = player_data['highest scoring word']
                            player.best_game= player_data['best_game']
        except FileNotFoundError:
            pass


    @classmethod
    def create(cls, name):
        if name in cls.players:
            print(f"There is already a player called {name}. Please choose another name.")
            return None
        player = cls(name)
        cls.players[name] = player
        return player

    
    def to_dict(self):
        return {'name': self.name, 'points': self.points, 'games won': self.games_won, 'games lost': self.games_lost, 'highest scoring word': self.highest_scoring_word, 'best game': self.best_game}
    @classmethod
    def save(cls):
        #save players data
        try:
            print(f"Saving data...")
            data = {name: player.to-dict() for name, player in cls.players.items()}
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=2)
        except:
            print('error')
