import threading

class Area:
    # Initializes the area with the first room available. Should implement a savefile load here.
    def __init__(self, json):
        self.rooms = json
        self.current_room = self.search_room(1)
        
    def search_room(self, input):
        for item in self.rooms:
            if item["id"] == input:
                return item
        print("no rooms found")        

class DictionaryHandler:
    def __init__(self, dictionaryJson):
        self.dictionary = dictionaryJson
    
    def get_term(self, termset_name, term_name):
        termset = self.dictionary.get(termset_name)
        if termset:
            term = termset.get(term_name)
            return term

class ActionHandler:
    def __init__(self, engine):
        self.engine = engine
        
    def move(self, args):        
        direction = self.engine.dictionary.get_term("directions", args[0])
        if not direction:
            print("You can't move in that direction.")
            return
        
        exits = self.engine.area.current_room.get("exits")
        if not exits:
            print("You are trapped! You cannot see any exit in this room!")
            return
        
        next_room = exits.get(direction)
        if not next_room:
            print("There are no exits there.")
            return
    
        room = self.engine.area.search_room(next_room)
        self.engine.area.current_room = room
        print(f"You move {direction}")

class Engine:
    def __init__(self, areasJson, dictionaryJson):
        self.area = Area(areasJson)
        self.dictionary = DictionaryHandler(dictionaryJson)
        self.action_handler = ActionHandler(self)
        self.tick()
                        
    def tick(self):
        self.tick_thread = threading.Timer(interval=3, function=self.tick)
        self.tick_thread.start()
        
    def cancel_tick_thread(self):
        print("Canceling tick thread..")
        self.tick_thread.cancel()
        
    def quit(self):
        self.cancel_tick_thread()
        print("Quitting game..")
        
    def get_tokens(self, input):
        return input.split(" ") 
        
    def remove_command_token(self, tokens):
        tokens.pop(0)
    
    def manage_action(self, input):
        if(len(input) > 30):
            print("Too many arguments")
            return
        input = input.lower()
        tokens = self.get_tokens(input)
        command_token = tokens[0]
        command = self.dictionary.get_term("commands", command_token)
        if(command):
            json_parameters = command.get("parameters")
            parameters = []
            if(json_parameters):
                split_parameters = json_parameters.split("|")
                parameters = split_parameters
            else:
                self.remove_command_token(tokens)
                parameters = tokens
            method = command.get("method")
            if not method: 
                return
            getattr(self.action_handler, method)(parameters)

    def print_room(self):
        print(self.area.current_room.get("description"))
        exits = self.area.current_room.get("exits")
        if exits:
            print("Exits:", end='')
            for exit in exits:
                formattedExit = "[" + exit[:1].capitalize() + "]" + exit[1:] 
                print(f" {formattedExit}", end='')
            print("")

                
