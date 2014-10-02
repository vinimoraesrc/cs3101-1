# Prints a nested list showing different indentations for each level.
# Recursively traverses the nested list, accumulating a value to
# represent the number of dots to be printed whenever the recursion
# reaches a new step, i.e. finds another nested list.
# Item (a)
def print_nlist(nlist):

    def print_sub(curr, indent):
        if isinstance(curr, list): # Analogous to if type(curr) is list
            for i in curr:
                print_sub(i, (indent + 4))
        else:
            print ("."*indent + str(curr))

    for x in nlist:
        print_sub(x,1)

# Recursively applies a function to the elements of the nested list.
# Searches for the elements which are not lists and then applies
# the given function, keeping track of the 'depth' of the list in which
# the element is contained.
# Item (b)
def map_nlist(nlist, fun):

    tmp = list()

    def apply(curr, fun, aux):
        if isinstance(curr, list): # Analogous to if type(curr) is list
            for i in curr:
                aux += (apply(i, fun, list()))
            return [aux]
        else:
            curr = fun(curr)
            aux.append(curr)
            return aux

    for x in nlist:
        tmp += (apply(x, fun, list()))

    return tmp

# Recursively applies a (binary) combiner to the elements of the list.
# Folds the nested list, recursively applying the combiner to the
# elements.
# Item (c)
def combine_nlist(nlist, init, combiner):

    result = init

    def combine(curr, value, combiner):
        if isinstance(curr, list): # Analogous to if type(curr) is list
            for i in curr:
                value = combine(i, value, combiner)
            return value
        else:
            return combiner(value, curr)

    for x in nlist:
        result = combine(x, result, combiner)

    return result

# Transforms a nested list into a simple one.
# Simply uses the combine_nlist function with a concatenation combiner.
# Item (d)
def flatten_nlist(nlist):
    return combine_nlist(nlist, [], lambda x, y: x + [y])


# Tests below

nlist = [1, [2, [3, [4, 5]]], [6, [7, [8, [9]], 10]]]

print_nlist(nlist)

t = map_nlist(nlist, lambda x: x*2)
print (t)

x = combine_nlist([1,[2, [5, 6, 7]]], 0, lambda x,y: x + y)
print (x)

l = flatten_nlist(nlist)
print (l)
