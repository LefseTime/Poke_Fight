def intro_texts():
    texts = ["Welcome to the wonderful world of JoeToe!",
            "My name is Scholar Tree, and I'll be your guide!"]    
    return texts

def types():
    types = ["SquirtGun", "CharMangler", "BulbousSore", "MagiKrap"]
    return types

def prompt_name(type):
    texts = ["Your new {} looks up at you adoringly.".format(type), "In the distance, a wild MulletEagle screeches, a squirming MontyPython clasped in its strong, strong talons.","A single tear rolls down your cheek.", "What would you like to name your precious {}? ".format(type)]
    return texts

def prompt_sad(name):
    texts = ["{} looks concerned about your judgment.".format(name.title()), "What sound does {} make in its confusion? ".format(name.title())]
    return texts

def prompt_happy(name):
    texts = ["'Oh my sweet {}!' you think.".format(name.title()), "Overcome with emotion, you sweep {} up in a loving embrace.".format(name.title()), "{} makes a happy sound: ".format(name.title())]
    return texts

def encounterWildPoke(wild_poke):
    texts = ["Suddenly a {} appears.".format(wild_poke.name), "The {} wants to have a...".format(wild_poke.name), "POKE_FIGHT™", "Suddenly you realize...", "THAT IS THE NAME OF THIS APP!!!!"]
    return texts
