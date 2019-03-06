def intro_texts():
    texts = ["Welcome to the wonderful world of JoeToe!",
            "My name is Scholar Tree, and I'll be your guide!", 
            "Would you like to be serenaded with the lengthy and unique Song of my People before we get down to nuts and bolts?"]    
    return texts

def types():
    types = ["SquirtGun", "CharMangler", "BulbousSore", "MagiKrap"]
    return types

def prompt_name(type):
    texts = ["Your new {} looks up at you adoringly.".format(type), "In the distance, a wild MulletEagle screeches, a squirming MontyPython clasped in its strong, strong talons.","A single tear rolls down your cheek.", "What would you like to name your precious {}? ".format(type)]
    return texts