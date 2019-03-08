from logic import initializeUserPoke, createWildPoke, regenerate, randomMove
import flask_ui as ui
from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap
from fight import Round, RoundResult
import random


def newRound(user_move, user_attack, user_defense, user_speed, user_hp, wild_attack, wild_defense, wild_speed, wild_hp, user_name, wild_name):

    if user_move == "4":
        user_move = randomMove()
    wild_move = randomMove()
    result = RoundResult(user_hp, wild_hp, wild_move)

    if user_move == "2":
        user_defense = defend(user_defense)
        user_hp = regenerate(user_hp)
        result.texts.append("{} is defending!".format(user_name))
        result.texts.append("{} regenerates HP to {}!".format(user_name, user_hp))
    elif user_move == "3":
        result.texts.append("{} is flopping about uselessly!".format(user_name))

    if wild_move == "2":
        wild_defense = defend(wild_defense)
        wild_hp = regenerate(wild_hp)
        result.texts.append("{} is defending!".format(wild_name))
        result.texts.append("{} regenerates HP to {}!".format(wild_name, wild_hp))
    elif wild_move == "3":
        result.texts.append("{} is flopping about uselessly!".format(wild_name))

    if user_move == "1" and wild_move == "1":
        first_move = determineOrder(user_speed, wild_speed)
        result.first_move = first_move
        if first_move == "user":
            wild_hp = attack(user_attack, wild_defense, wild_hp)
            result.wild_hp = wild_hp
            result.texts.append("{} attacks, bringing {}'s HP to {}!".format(user_name, wild_name, wild_hp))
            if wild_hp <= 0:
                result.texts.append("{} passes out!".format(wild_name))
                return result
            user_hp = attack(wild_attack, user_defense, user_hp)
            result.user_hp = user_hp
            result.texts.append("{} attacks, bringing {}'s HP to {}!".format(wild_name, user_name, user_hp))
        else:
            user_hp = attack(wild_attack, user_defense, user_hp)
            result.user_hp = user_hp
            result.texts.append("{} attacks, bringing {}'s HP to {}!".format(wild_name, user_name, user_hp))
            if user_hp <= 0:
                result.texts.append("{} passes out!".format(user_name))
                return result
            wild_hp = attack(user_attack, wild_defense, wild_hp)
            result.wild_hp = wild_hp
            result.texts.append("{} attacks, bringing {}'s HP to {}!".format(user_name, wild_name, wild_hp))

    elif user_move == "1":
        wild_hp = attack(user_attack, wild_defense, wild_hp)
        result.wild_hp = wild_hp
        result.texts.append("{} attacks, bringing {}'s HP to {}!".format(user_name, wild_name, wild_hp))
        if wild_hp <= 0:
                result.texts.append("{} passes out!".format(wild_name))
                return result
    elif wild_move == "1":
        user_hp = attack(wild_attack, user_defense, user_hp)
        result.user_hp = user_hp
        result.texts.append("{} attacks, bringing {}'s HP to {}!".format(wild_name, user_name, user_hp))
        if user_hp <= 0:
                result.texts.append("{} passes out!".format(user_name))
                return result

    return result


def determineOrder(user_speed, wild_speed):
    user_speed = user_speed * random.randint(0, 3)
    wild_speed = wild_speed * random.randint(0, 3)

    if user_speed >= wild_speed:
        return "user"
    else:
        return "wild"


def defend(poke_defense):
    return int(poke_defense * (random.randint(2, 4)/2))

def attack(attacker_attack, def_def, def_hp):
    att_pwr = attacker_attack + random.randint(-1, 4)
    difference = att_pwr - def_def

    if difference < 2:
        difference = 2
    def_hp = def_hp - difference
    return int(def_hp)