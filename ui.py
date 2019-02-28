from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap
import random

def createPoke():
    valid = False
    while not valid:
        type_num = input("------------\n   Pokes  \n------------\n  1. SquirtGun\n  2. CharMangler\n  3. BulbousSore\n  4. MagiKrap\n------------\nWhich Poke do you choose? ")
        if type_num == "1" or type_num == "SquirtGun":
            type = "SquirtGun"
            valid = True
        elif type_num == "2" or type_num == "CharMangler":
            type = "CharMangler"
            valid = True
        elif type_num == "3" or type_num == "BulbousSore":
            type = 'BulbousSore'
            valid = True
        elif type_num == "4" or type_num == "MagiKrap":
            type = 'MagiKrap'
            valid = True

    print("\nYour new {} looks up at you adoringly.\nIn the distance, a wild MulletEagle screeches, and a single tear rolls down your cheek.".format(type))
    name = str(input("\nWhat would you like to name your precious {}? ".format(type))).title()
    sad_sound = str(input("\n{} looks concerned about your judgment. What sound does {} make in its confusion? ".format(name,name)))
    happy_sound = str(input("\n'Oh my sweet {}!' you think. Overcome with emotion, you sweep {} up in a loving embrace.\n{} makes a happy sound: ".format(name,name,name)))
    print("'{}! {} indeed, you beautiful little {},' you coo.".format(happy_sound.title(), happy_sound.title(),type))

    if type == "SquirtGun":
        user_poke = SquirtGun(name, happy_sound,sad_sound)
    elif type == "CharMangler":
        user_poke = CharMangler(name,happy_sound,sad_sound)
    elif type == "BulbousSore":
        user_poke = BulbousSore(name,happy_sound,sad_sound)
    elif type == "MagiKrap":
        user_poke = MagiKrap(name,happy_sound,sad_sound)

    return user_poke


def createWildPoke():
    types = ["SquirtGun","CharMangler","BulbousSore","MagiKrap"]
    type = random.choice(types)
    if type == "SquirtGun":
        return SquirtGun("SquirtGun", "pew pew", "squish")
    elif type == "BulbousSore":
        return BulbousSore("BulbousSore", "mwow", "*festers squishily*")
    elif type == "CharMangler":
        return CharMangler("CharMangler", "eheheheh", "mmmmmnnnnn")
    elif type == "MagiKrap":
        return MagiKrap("MagiKrap", "*flop*", "*flop flop*")
    

def fight(user, wild):
    finished = False
    user_hp = user.hp
    wild_hp = wild.hp
    while not finished:
        bround(user, wild, user_hp, wild_hp)
        if user_hp == 0:
            winner ="Wild"
            finished = True
        elif wild_hp == 0:
            winner = "User"
            finished = True
    

def bround(user, wild, user_hp, wild_hp):
    
    
