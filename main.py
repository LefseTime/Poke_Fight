from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap
import ui

user_poke = ui.createPoke()
input("\nYou hear a rustling in the grass...")
wild_poke = ui.createWildPoke()
print("\nSuddenly a wild {} appears. The {} wants to have a Poke_Fight™! That is the name of this app!".format(wild_poke.type,wild_poke.type))