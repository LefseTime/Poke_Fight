from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
import ui
import logic


type = ui.chooseType
name = ui.chooseName(type)
happy_sound = ui.chooseHappy(name)
sad_sound = ui.chooseSad(name)

user_poke = logic.initializeUserPoke(type, name, happy_sound, sad_sound)
wild_poke = logic.createWildPoke()

ui.encounterWildPoke(wild_poke)
logic.fight(user_poke, wild_poke)
