"""Module containing a decoding function.
"""

# NOTE: Examples for Question 3(b) provided in the form f comments
# inside the main function.

from gen_key import Key
import sys

try:
   import cPickle as pickle
except:
   import pickle


def decode(encoded_msg, key):
    cypher_dict = dict(key.cypher)

    # Inverts the dictionary. Way better than my previous solution in
    # homework 2.
    inv_dict = dict((y, x) for x, y in cypher_dict.items()) 

    decoded_msg = ""

    for i in encoded_msg:
        try:
            l = len(i)
        except TypeError:
            print ("Invalid element found in outer list. Skipping it.")
        else:
            try:
                c = inv_dict[l]
            except KeyError:
                print ("Too many elements in one of lists. Skipping it.")
            else:   
                decoded_msg += c

    return decoded_msg

def main():
    input_file = sys.argv[1]
    key_file = sys.argv[2]

    with open(input_file, 'rb') as f: # Unpickle encoded message
        msg = pickle.load(f)

    with open(key_file, 'rb') as f: # Unpickle key
        key = pickle.load(f)

    # Question 3 part (b), 1.
    # Example of an object which causes this exception: msg = 5

    # Question 3 part (b), 2.
    # Example of an object which causes this exception: msg = [[1],5]

    # Question 3 part (b), 2.
    # Example of an object which causes this exception: 
    # msg = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
    #        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1], [1, 1]]

    try:
         decoded_msg = decode(msg, key)
         print (decoded_msg)
    except TypeError:
        print ("Encrypted message is not a list at all.")

if __name__ == "__main__":
    main()
