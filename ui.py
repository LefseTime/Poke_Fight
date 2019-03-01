from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap

def createUserPoke():
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

def chooseMove(poke):
    valid = False
    while not valid:
        move = input('Would you like {} to attack(1), defend and regenerate hp(2), or choose for itself(3)? '.format(poke.name))
        if move == "1" or move == "2" or move == "3":
            valid = True
            return move


def encounterWildPoke(wild_poke):
    print("\nSuddenly a wild {} appears. The {} wants to have a Poke_Fight™!\nSuddenly you realize... that is the name of this app!".format(wild_poke.type,wild_poke.type))