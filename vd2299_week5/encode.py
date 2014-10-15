"""Module containing an encoding function.
"""

from gen_key import Key
import sys

try:
   import cPickle as pickle
except:
   import pickle

class EncodingException(Exception):
    """ Exception that indicated invalid characters in the message.
    """

def encode(msg, key):
    encoded_msg = list()

    cypher_dict = dict(key.cypher) # Creates a dict from the tuple list

    for i in msg.upper():

        if (not i.isalpha()) and (i != ' '):
            raise EncodingException (i + " is an invalid symbol.")

        else:
            tmp = list()

            for n in range(cypher_dict[i]):
               tmp.append('1')

            encoded_msg.append(tmp)

    return encoded_msg

def main():

    output_file = sys.argv[1]
    key_file = sys.argv[2]

    while (1): # Queries the user until he/she types in a valid input.
        try:
            with open(key_file, 'rb') as f: # Unpickle key
                key = pickle.load(f)

            msg = str(input("Type a message:"))
            encoded_msg = encode(msg, key)

        except EncodingException:
            print ("Please, use only letters and whitespaces.")

        else:
            break

    with open(output_file, 'wb') as f:
        pickle.dump(encoded_msg, f, protocol = 2)

if __name__ == "__main__":
    main()