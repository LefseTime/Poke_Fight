from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
import ui
import logic


poke_type = ui.chooseType()
name = ui.chooseName(poke_type)
sad_sound = ui.chooseSad(name)
happy_sound = ui.chooseHappy(name, poke_type)


user_poke = logic.initializeUserPoke(poke_type, name, happy_sound, sad_sound)
wild_poke = logic.createWildPoke()

ui.encounterWildPoke(wild_poke)
logic.fight(user_poke, wild_poke)
