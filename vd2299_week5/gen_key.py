"""Module containing an encryption class.
"""

import random
import string
import sys

try:
   import cPickle as pickle
except:
   import pickle

class Key(dict):

    def __init__(self):
        characters = list(string.ascii_uppercase)
        characters.append(' ')
        random.shuffle(characters)
        self.cypher = zip(characters, range(27))

def main():
    specified_file = sys.argv[1]
    key = Key()

    with open(specified_file, 'wb') as f:
        pickle.dump(key, f, protocol = 2)

if __name__ == "__main__":
    main()
