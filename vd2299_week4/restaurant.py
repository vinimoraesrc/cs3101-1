class Guest(object):

    def __init__(self, name, init_hunger):
        self.name = name
        self.hunger = init_hunger

    def eat(self):
        if (self.hunger > 0): self.hunger -= 1
        if (self.hunger == 0):
            print (self.name + ": Burp!") # Guest is sated
        return self.hunger

class Restaurant(list):

    def __init__(self, size):
        self.size = size
        list.__init__(self, list()) # Calls list() init method

        for i in range(self.size):
            self.append(None)

    def seat(self, guest):

        for i in range(self.size): # Iterates through tables
            if (self[i] == None):
                self[i] = guest
                print ("Seating guest " + guest.name + " at table " + str(i) + ".")
                return True

        print ("No free table.")
        return False

    def serve(self):

        for i in range(self.size): # Iterates through tables
            if (self[i] != None):
                print ("Serving guest " + self[i].name + ".")
                self[i].eat()
                if (self[i].hunger == 0): # Guest is sated and leaves.
                    self[i] = None
                return

        print ("No guest to serve.")
