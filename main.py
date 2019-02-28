from poke import Poke, BulbousSore, CharMangler, SquirtGun, MagiKrap

bulb = BulbousSore("Bulb","aaa","bbb")

print(bulb.name)

valid = False
type = "error"
while not valid:
    type_num = input("------------\n   Pokes  \n------------\n  1. SquirtGun\n  2. CharMangler\n  3. BulbousSore\n  4. MagiKrap\n------------\nWhich Poke do you choose? ")
    if type_num == '1' or "SquirtGun":
        type = "SquirtGun"
        valid = True
    elif type_num == '2' or "CharMangler":
        type = "CharMangler"
        valid = True
    elif type_num == '3' or "BulbousSore":
        type = 'BulbousSore'
        valid = True
    elif type_num == '4' or "MagiKrap":
        type = 'MagiKrap'
        valid = True

print(type)