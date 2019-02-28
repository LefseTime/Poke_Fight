class Poke:
    def __init__(self, name, happy_sound, sad_sound):
        self.name = name
        self.happy_sound = happy_sound
        self.sad_sound = sad_sound

class BulbousSore(Poke):
    def __init__(self, name, happy_sound, sad_sound):
        super().__init__(name, happy_sound, sad_sound)
        self.attack = 5
        self.defense = 9
        self.speed = 6
        self.hp = 26
        self.type = "BulbousSore"

class CharMangler(Poke):
    def __init__(self, name, happy_sound, sad_sound):
        super().__init__(name, happy_sound, sad_sound)
        self.attack = 9
        self.defense = 4
        self.speed = 7
        self.hp = 20
        self.type = "CharMangler"

class SquirtGun(Poke):
    def __init__(self, name, happy_sound, sad_sound):
        super().__init__(name, happy_sound, sad_sound)
        self.attack = 7
        self.defense = 7
        self.speed = 5
        self.hp = 23
        self.type = "SquirtGun"

class MagiKrap(Poke):
    def __init__(self, name, happy_sound, sad_sound):
        super().__init__(name, happy_sound, sad_sound)
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.hp = 0
        self.type = "MagiKrap"