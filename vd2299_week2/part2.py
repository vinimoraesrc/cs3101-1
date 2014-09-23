fruit_to_color = {'banana' : 'yellow', 
                  'blueberry' : 'blue', 
                  'cherry' : 'red', 
                  'lemon' : 'yellow', 
                  'kiwi' : 'green', 
                  'strawberry' : 'red', 
                  'tomato' : 'red'}

def color_to_fruits(color):
    """Creates a dictionary that maps color to lists of fruits.

    Argument:
    color -- the color which will be queried.

    The function initializes an empty dictionary and iteratively
    builds it by going through the fruit_to_color dict. If an element
    has not yet been initialized, the function assigns a new object
    to the unseen element (key), thus initializing it.
    """

    keys = fruit_to_color.keys()

    fruits = {}

    for i in keys:

        current_color = fruit_to_color[i]

        if current_color == color:

            if current_color not in fruits:
                fruits[current_color] = [i]

            else:
                fruits[current_color] += [i]

    print (fruits[color])
   

color_to_fruits('yellow')
