from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap
import logic

def chooseType():
    valid = False
    while not valid:
        type_num = input("-----------------\n   Pokes  \n-----------------\n  1. SquirtGun\n  2. CharMangler\n  3. BulbousSore\n  4. MagiKrap\n-----------------\nWhich Poke do you choose? ")
        if type_num == "1" or type_num == "SquirtGun":
            poke_type = "SquirtGun"
            valid = True
        elif type_num == "2" or type_num == "CharMangler":
            poke_type = "CharMangler"
            valid = True
        elif type_num == "3" or type_num == "BulbousSore":
            poke_type = 'BulbousSore'
            valid = True
        elif type_num == "4" or type_num == "MagiKrap":
            poke_type = 'MagiKrap'
            valid = True
    return poke_type

def chooseName(type):
    print("\nYour new {} looks up at you adoringly.\nIn the distance, a wild MulletEagle screeches, and a single tear rolls down your cheek.".format(type))
    name = str(input("\nWhat would you like to name your precious {}? ".format(type))).title()
    return name

def chooseSad(name):
    sad_sound = str(input("\n{} looks concerned about your judgment. What sound does {} make in its confusion? ".format(name,name)))
    return sad_sound

def chooseHappy(name, type): 
    happy_sound = str(input("\n'Oh my sweet {}!' you think. Overcome with emotion, you sweep {} up in a loving embrace.\n{} makes a happy sound: ".format(name,name,name)))
    input("'{}! {} indeed, you beautiful little {},' you coo.".format(happy_sound.title(), happy_sound.title(),type))
    return happy_sound

def chooseMove(poke):
    valid = False
    while not valid:
        move = input('Would you like {} to attack(1), defend and regenerate hp(2), or choose for itself(3)? '.format(poke.name))
        if move == "1" or move == "2" or move == "3":
            return move

def displayHpStatus(user_name, wild_type, user_hp, wild_hp):
    print("\n---------------\n  HP Status  \n---------------\n{}: {}\nWild {}: {}\n".format(user_name, str(user_hp), wild_type, str(wild_hp)))

def encounterWildPoke(wild_poke):
    input("\nSuddenly a wild {} appears. The {} wants to have a Poke_Fight™!".format(wild_poke.type,wild_poke.type))
    input("\nSuddenly you realize... ")
    input("\n\t...that is the name of this app!")

def displayDefense(poke, hp):
    input("{} is defending! {} regenerates HP back up to {}!".format(poke, poke, hp))

def displayAttack(attacker, defender, hp):
    input("{} attacks, bringing {}'s HP to {}!".format(attacker.name, defender.name, hp))