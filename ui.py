def createPoke():
    valid = False
    while not valid:
        type_num = input("------------\n   Pokes  \n------------\n  1. SquirtGun\n  2. CharMangler\n  3. BulbousSore\n  4. MagiKrap\n------------\nWhich Poke do you choose? ")
        if type_num == "1" or type_num == "SquirtGun":
            type = "SquirtGun"
            valid = True
        elif type_num == "2" or type_num == "CharMangler":
            type = "CharMangler"
            valid = True
        elif type_num == "3" or type_num == "BulbousSore":
            type = 'BulbousSore'
            valid = True
        elif type_num == "4" or type_num == "MagiKrap":
            type = 'MagiKrap'
            valid = True

    print("\nYour new {} looks up at you adoringly.\nIn the distance, a wild MulletEagle screeches, and a single tear rolls down your cheek.".format(type))
    name = str(input("\nWhat would you like to name your precious {}? ".format(type)))