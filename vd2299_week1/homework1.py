###############################################
# COMS3101.001 - Python - Homework 1
#
# Please fill in your solutions for part 2 to 4 
# below. 

##############################################################################
# Part 2
# For each line in the following interactive Python interpreter session, write
# a short justification for the output, clearly indicating which objects are
# in memory and which variables refer to them (ignore garbage collection for
# this exercise)
# Add your explanations as a new comment after each line. 

#>>> y,x = [1], [1]
#>>> x is y
#False

# The line outputs False because, even though x and y have the same 
# value, they refer to different objects in memory, and the operator
# 'is' tests for object equality. If the operator == was used instead,
# it would evaluate True, since it tests for value equality. 
# There are two objects in memory, both having [1] as a value. 
# The variable y refers to one of them and x refers to the other one.

#>>> x = y
#x is y
#True

# The line outputs True because x is now referring to the same object
# as the one referred to by y (by calling x = y) and now the object
# equality holds. Since the garbage collector is being ignored, there
# are still two objects in the memory, both having [1] as a value.
# Both x and y point to the same object, and one of them is referred
# by no variable.

#>>> y = y + x
#>>> x.append(y)
#>>> x == y
#False

# The line outputs False because y now has a value of [1,1] while
# x has a value of [1,[1,1]], so the test for value does not hold true.
# Since the append function does not create new lists and the
# + operation does, we now have 3 objects in memory: 
# one with a [1,1] value, to which y points; one with a [1,[1,1]] value
# to which x points and one with a [1] value to which no variale points.



##############################################################################
# Part 3 - Lists and for-Loops
#
# Use two nested for loops to compute the value 
# of expressions of the form 
# (a[1]+...+a[m])*(b[1]+...+b[m]).
# 
# Assume that a and b are arbitrary sequences of numbers.
# For instance, for a = [1, 2, 4] and b = [2, 3] the result would be 35.

a = [1, 2, 4]
b = [2, 3]
#Your code starts here
r = 0
for x in a:
    tmp = 0
    for y in b:
        tmp += (x*y)
    r += tmp
print (r)
#Your code ends here


##############################################################################
# Part 4 - Loops, Strings, and Indices
#
# Given a string s create a second string s2 that is a copy of s but without 
# characters that have an identical element next to them.
#
# For instance the, string
# s = "abbcaabcaa"
# should produce the answer "acbc".
#
# Pay attention to the first and last element.
# 
# Instead of iterating over elements of s, you should iterate over
# indices of s (use range). This should work for arbitrary sequences of
# arbitary length. You can refer to a specific character in a string 
# using the index operation s[index]. The index of the first character is 0.
# In the above example s[0] equals 'a' and s[3] equals 'c'.
s = 'abbcaabcaa'
#Your code starts here
length = len(s)
s2 = ""

# The function iterates through the indices of s as suggested
# and checks whether the next or the previous element in s
# is equal to the element at the current index, paying
# special attention to the first and last elements (avoiding
# "nullpointers").

for i in range(length):
    if (i < (length - 1)) and (i > 0):
        if (s[i] != s[i+1]) and (s[i-1] != s[i]):
            s2 += s[i]

    elif (i == (length - 1)): # Paying attention to the last element
        if s[i] != s[i-1]:
            s2 += s[i]

    elif i == 0: # Paying attention to the first element
        if s[i] != s[i+1]:
            s2 += s[i]

print (s2)    
#Your code ends here