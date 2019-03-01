from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
import ui, logic, sys


def newUserPoke():
    poke_type = ui.chooseType()
    name = ui.chooseName(poke_type)
    sad_sound = ui.chooseSad(name)
    happy_sound = ui.chooseHappy(name, poke_type)

    return logic.initializeUserPoke(poke_type, name, happy_sound, sad_sound)


ballad = ui.intro()

if ballad == "y" or ballad == "yes":
    ui.songOfPeople()

user_poke = newUserPoke()

keepGoing = True
create_new = "none"
while keepGoing:

    if create_new == "y" or create_new == "yes":
        user_poke = newUserPoke()

    wild_poke = logic.createWildPoke()

    ui.encounterWildPoke(wild_poke)
    result = logic.fight(user_poke, wild_poke)

    if result == "win":
        again = ui.win(user_poke)
        if again == "no" or again == "n":
            keepGoing = False
            break
        else:
            create_new = ui.newPokeOption(user_poke)
    elif result == "lose":
        again = ui.lose(user_poke)
        if again == "no" or again == "n":
            keepGoing = False
            break
        else:
            create_new = ui.newPokeOption(user_poke)

ui.exit(user_poke)
sys.exit()



