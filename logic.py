from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap
import random
import ui

def initializeUserPoke(type, name, happy, sad):

    if type == "SquirtGun":
        return SquirtGun(name, happy, sad)
    elif type == "CharMangler":
        return CharMangler(name, happy, sad)
    elif type == "BulbousSore":
        return BulbousSore(name, happy, sad)
    elif type == "MagiKrap":
        return MagiKrap(name,happy,sad)


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
    user_hp = int(user.hp)
    wild_hp = int(wild.hp)
    while not finished:
        ui.displayHpStatus(user.name, wild.type, user_hp, wild_hp)
        user_move = ui.chooseMove(user)
        if user_move == "3":
            user_move = randomMove()
        wild_move = randomMove()




        if user_hp == 0:
            winner ="Wild"
            finished = True
        elif wild_hp == 0:
            winner = "User"
            finished = True
    print(winner)


    

def randomMove():
    return str(random.randint(1,2))
    


    
