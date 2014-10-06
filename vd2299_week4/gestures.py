import random

class Rock(object):

    def __init__(self):
        self.type = 0 # Avoid using isinstance and facilitate operation 

    def __lt__(self, other):
        return (other.type == 2)

    def __gt__(self, other):
        return (other.type == 1)

    def __eq__(self, other):
        return (other.type == self.type)

    def __str__(self):
        return "Rock"

class Scissors(object):

    def __init__(self):
        self.type = 1

    def __lt__(self, other):
        return (other.type == 0)
            
    def __gt__(self, other):
        return (other.type == 2)

    def __eq__(self, other):
        return (other.type == self.type)

    def __str__(self):
        return "Scissors"

class Paper(object):

    def __init__(self):
        self.type = 2

    def __lt__(self, other):
        return (other.type == 1)
            
    def __gt__(self, other):
        return (other.type == 0)

    def __eq__(self, other):
        return (other.type == self.type)

    def __str__(self):
        return "Paper"

class Player(object):

    def play(self):
        # Dict relating numeric type to object type
        choices = {'0': Rock(), '1': Scissors(), '2': Paper()}

        rdm = random.choice(range(0, 3))
        return choices[str(rdm)]

class HumanPlayer(Player):

    def play(self):
        # Dict relating numeric type to object type
        choices = {'Rock': Rock(), 'Scissors': Scissors(), 'Paper': Paper()}

        move = input("Choose a move (Rock, Paper or Scissors): ")

        while move not in choices: # User has to choose valid move
            move = input("Type a valid move (Rock, Paper or Scissors):")

        return choices[move]

def main():
    pc = Player()
    p1 = HumanPlayer()

    sc1, sc2 = 0, 0

    # Assumes the game goes on "forever" (since it was not specified).
    # User can quit by quitting the python program itself.
    while True:
        m1 = p1.play()
        print ("\nYou chose " + str(m1))
        m2 = pc.play()
        print ("AI played " + str(m2) + '\n')

        if (m1 == m2):
            print ("Tie! Nobody wins points.\n")
        elif (m1 > m2):
            print ("You won!\n")
            sc1 += 1
        else:
            print ("AI won!\n")
            sc2 += 1

        print ("Player: {0} | AI: {1}".format(sc1, sc2))

if __name__ == "__main__":
    main()