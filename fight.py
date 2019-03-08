class RoundResult:
    def __init__(self, user_hp, wild_hp, wild_move):
        self.user_hp = user_hp
        self.wild_hp = wild_hp
        self.wild_move = wild_move
        self.first_move = "null"
        self.texts = []

class Round:
    def __init__(self, user, user_hp, wild, wild_hp):
        self.user = user
        self.user_hp = user_hp
        self.wild = wild
        self.wild_hp = wild_hp
