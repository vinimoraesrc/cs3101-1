
# Schoenfinkeling decorator
def schoenfinkeled(fun):

    def new_fun(args):
        try:
           return fun(args)

        except TypeError:

            # Returns a function with n-1 arguments
            aux = lambda *myArgs: fun(args, *myArgs)

            # Recursively applies schoenfinkeling
            return schoenfinkeled(aux)

    return new_fun

@schoenfinkeled
def myfun(a,b,c):
    return a + b + c

# TypeError
#print(myfun(1, 2, 3))

f = myfun(11)(1)(2)
print (f)

g = myfun(77)
h = g(1)
i = h(4)
print (i)