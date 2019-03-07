from logic import initializeUserPoke, createWildPoke, determineOrder, defend, regenerate, attack, randomMove
import flask_ui as ui
from poke import Poke, BulbousSore, SquirtGun, CharMangler, MagiKrap
from fight import Round, Fight
import random

def initializeFight(user, wild):
    p_fight = Fight(user, wild)
    return p_fight

def newRound(user_move):
    user = p_fight.get__user()
    wild = p_fight.get__wild()

    if user_move == "4":
        user_move = randomMove()
    wild_move = randomMove()

    p_fight.set__user_move(user_move)
    p_fight.set__wild_move(wild_move)

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
                return Round(user, user_hp, wild, wild_hp)
            user_hp = attack(wild, user_defense, user_hp)
            ui.displayAttack(wild, user, user_hp)
        else:
            user_hp = attack(wild, user_defense, user_hp)
            ui.displayAttack(wild, user, user_hp)
            if user_hp <= 0 or wild_hp <= 0:
                return Round(user, user_hp, wild, wild_hp)
            wild_hp = attack(user, wild_defense, wild_hp)
            ui.displayAttack(user, wild, wild_hp)

    elif user_move == "1":
        wild_hp = attack(user, wild_defense, wild_hp)
        ui.displayAttack(user, wild, wild_hp)
    elif wild_move == "1":
        user_hp = attack(wild, user_defense, user_hp)
        ui.displayAttack(wild, user, user_hp)

    return p_fight
