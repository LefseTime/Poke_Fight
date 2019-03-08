from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap

def chooseType():
    input("Well, well then! Looks like you'll need a Poke, lil' whippersnapper!")
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
    print("\nYour new {} looks up at you adoringly.\nIn the distance, a wild MulletEagle screeches, a squirming MontyPython clasped in its strong, strong talons, and a single tear rolls down your cheek.".format(type))
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
        move = input('Would you like {} to attack(1), defend and regenerate hp(2), flail helplessly(3), or choose for itself(4)? '.format(poke.name))
        if move == "1" or move == "2" or move == "3" or move == "4":
            return move

def displayHpStatus(user_name, wild_type, user_hp, wild_hp):
    print("\n---------------\n  HP Status  \n---------------\n{}: {}\nWild {}: {}\n".format(user_name, str(user_hp), wild_type, str(wild_hp)))

def encounterWildPoke(wild_poke):
    input("\nSuddenly a {} appears. The {} wants to have a\n\n\t--------------------------------------------------------\n\t\t\t\tPOKE_FIGHT™  \n\t--------------------------------------------------------\n".format(wild_poke.type,wild_poke.type))
    input("\nSuddenly you realize... ")
    input("\n\t--------------------------------------------------------\n\t\t... THAT IS THE NAME OF THIS APP!!!!  \n\t--------------------------------------------------------\n")

def displayDefense(poke, hp):
    input("{} is defending! {} regenerates HP back up to {}!".format(poke, poke, hp))

def displayAttack(attacker, defender, hp):
    input("{} attacks, bringing {}'s HP to {}!".format(attacker.name, defender.name, hp))

def flail(poke):
    input("{} flops about helplessly.".format(poke.name))

def win(poke):
    name = poke.name
    cap_sound = poke.happy_sound.title()
    sound = poke.happy_sound.lower()
    input("\nYou win! {} looks up at you, eyes misting over. '{}, {}!' For the first time in your life, you allow the tears to stream freely down your stoic face. '{}, {}...' you whisper back.".format(name, cap_sound,sound,cap_sound,sound))
    return input("Continue beating up wild Pokes? (y/n) ")

def lose(poke):
    name = poke.name
    cap_sound = poke.sad_sound.title()
    sound = poke.sad_sound.lower()
    input("\nYou lose! {} looks up at you, eyes misting over. '{}, {}!' For the first time in your life, you allow the tears to stream freely down your stoic face. '{}, {}...' you whisper back.".format(name, cap_sound,sound,cap_sound,sound))
    return input("Continue beating up wild Pokes? (y/n) ")

def newPokeOption(poke):
    return input("Throw away {} like a piece of garbage and continue with a new Poke? (y/n) ".format(poke.name))

def intro():
    input("\n\n\n\t--------------------------------------------------------\n\t\t\t\tPOKE_FIGHT™  \n\t--------------------------------------------------------\n\t\t\t(press enter to continue)\n")
    input("Welcome to the wonderful world of JoeToe!")
    input("My name is Scholar Tree, and I'll be your guide!")
    return input("Would you like to be serenaded with the lengthy and unique Song of my People before we get down to nuts and bolts? (y/n) ")

def songOfPeople():
    print("\n🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵")
    input("I hope to be the top one, like no one else waaaas!!!!")
    input("To teach them is my true test, to catch them is my purpooooosssseee!!!!!!")
    input("I will journey around the earth, looking far awaaaaayyyyyyy!!!!!")
    input("Every Poke, to comprehend the strength that's withiiiiinnn!!!!!")
    input("\nPOKES!!!!!")
    input("\nOoh, you're my favorite companion in a land we must proteeeccctttt!!!")
    input("\nPOKES!!!!!")
    input("\nHave to trap all of them!!!!")
    input("\nPOKES!!!!!")
    input("🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵🎵\n")

def exit(poke):
    sound = poke.sad_sound.lower()
    cap_sound = poke.sad_sound.title()
    input("\nIn your absence, the magical world of JoeToe slips into darkness and chaos.")
    input("\nThe evil 'Group Rock' rises to power, forcing thousands into questionable fashion choices and sadness.")
    input("\nEven {} is taken in, and grows a flowing soft mullet as you slowly slide from its memory.".format(poke.name))
    input("\n'{}, {}...' it cries sadly into its silken tresses each night. '{}, {}...'".format(cap_sound,sound,cap_sound,sound))
    input("\n\nFarewell, dear Trainer. You were our last hope, and you abandoned us. Farewell.\n\n\n\t--------------------------------------------------------\n\t\t\t\tTHE END  \n\t--------------------------------------------------------\n")