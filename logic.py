from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap
from fight import Round
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
        return MagiKrap(name, happy, sad)


def createWildPoke():
    types = ["SquirtGun", "CharMangler", "BulbousSore", "MagiKrap"]
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
    user_hp = int(user.hp)
    wild_hp = int(wild.hp)
    while user_hp > 0 and wild_hp > 0:
        new_round = Round(user, user_hp, wild, wild_hp)
        round_results = round(new_round)
        user_hp = round_results.user_hp
        wild_hp = round_results.wild_hp

    if user_hp <= 0:
        return "lose"

    elif wild_hp <= 0:
        return "win"


def round(new_round):
    user = new_round.user
    wild = new_round.wild
    user_hp = new_round.user_hp
    wild_hp = new_round.wild_hp

    ui.displayHpStatus(user.name, wild.type, user_hp, wild_hp)

    user_move = ui.chooseMove(user)
    if user_move == "4":
        user_move = randomMove()
    wild_move = randomMove()

    if user_move == "3":
        ui.flail(user)
    if wild_move == "3":
        ui.flail(wild)

    user_defense = user.defense
    wild_defense = wild.defense
    if user_move == "2":
        user_defense = defend(user)
        user_hp = regenerate(user_hp)
        ui.displayDefense(user.name, user_hp)
    if wild_move == "2":
        wild_defense = defend(wild)
        wild_hp = regenerate(wild_hp)
        ui.displayDefense(wild.name, wild_hp)

    if user_move == "1" and wild_move == "1":
        first_move = determineOrder(user, wild)
        if first_move.name == user.name:
            wild_hp = attack(user, wild_defense, wild_hp)
            ui.displayAttack(user, wild, wild_hp)
            if user_hp <= 0 or wild_hp <= 0:
                return
            user_hp = attack(wild, user_defense, user_hp)
            ui.displayAttack(wild, user, user_hp)
        else:
            user_hp = attack(wild, user_defense, user_hp)
            ui.displayAttack(wild, user, user_hp)
            if user_hp <= 0 or wild_hp <= 0:
                return
            wild_hp = attack(user, wild_defense, wild_hp)
            ui.displayAttack(user, wild, wild_hp)

    elif user_move == "1":
        wild_hp = attack(user, wild_defense, wild_hp)
        ui.displayAttack(user, wild, wild_hp)
    elif wild_move == "1":
        user_hp = attack(wild, user_defense, user_hp)
        ui.displayAttack(wild, user, user_hp)

    return Round(user, user_hp, wild, wild_hp)


def determineOrder(user, wild):
    user_speed = user.speed * random.randint(0, 3)
    wild_speed = wild.speed * random.randint(0, 3)

    if user_speed >= wild_speed:
        return user
    else:
        return wild


def defend(poke):
    return int(poke.defense * (random.randint(2, 4)/2))


def regenerate(hp):
    return int(hp + random.randint(0, 3))


def attack(attacker, def_def, def_hp):
    att_pwr = attacker.attack + random.randint(-1, 4)
    difference = att_pwr - def_def

    if difference < 2:
        difference = 2
    def_hp = def_hp - difference
    return int(def_hp)


def randomMove():
    return str(random.randint(1, 3))
