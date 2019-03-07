class Fight:
    def __init__(self, user, wild):
        self.user = user
        self.wild = wild
        self.user_move = 0
        self.wild_move = 0

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self__user = user

    def get_wild(self):
        return self.__wild

    def set_wild(self, wild):
        self__wild = wild

    def get_user_move(self):
        return self.__user_move

    def set_user_move(self, user_move):
        self__user_move = user_move

    def get_wild_move(self):
        return self.__wild_move

    def set_wild_move(self, wild_move):
        self__wild_move = wild_move

    



class Round:
    def __init__(self, user, user_hp, wild, wild_hp):
        self.user = user
        self.user_hp = user_hp
        self.wild = wild
        self.wild_hp = wild_hp
