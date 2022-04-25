import json
from engine import *

castleFile = open("castle.json")
dictionaryFile = open("dictionary.json")
areasJson = json.load(castleFile)
dictionaryJson = json.load(dictionaryFile)
engine = Engine(areasJson, dictionaryJson)
print(threading.current_thread)
while(1):
    print("")    
    engine.print_room()
    playerInput = input("> ")
    print(playerInput)
    engine.manage_action(playerInput)
    if(playerInput == "exit"):
        engine.quit()
        break
    