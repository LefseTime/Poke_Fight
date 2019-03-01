from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
import ui
import logic

user_poke = ui.createUserPoke()
wild_poke = logic.createWildPoke()
ui.encounterWildPoke(wild_poke)
logic.fight(user_poke, wild_poke)
