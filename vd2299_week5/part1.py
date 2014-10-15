import os
import sys

directory = sys.argv[1]
words = ["marijuana", "marihuana", "cannabis", "weed"]

# Recursively searches through directories for files containing
# incriminating words. Starts from the directory given as an argument
# through the command-line.

def search(current_dir):
    items = os.listdir(current_dir)

    for i in items:
        i_path = os.path.join(current_dir, i)

        if os.path.isfile(i_path): # If the item is a file, checks it
            for w in words:
                if w in i.lower():
                    print (i_path)

            if ("mary" in i.lower()) and ("jane" in i.lower()):
                print (i_path)

        elif os.path.isdir(i_path): # If it is a directory, searches it
            search(i_path)

search(directory)