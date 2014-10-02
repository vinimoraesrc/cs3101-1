# Generator function which acts as an iterator over ngrams of a string.
def ngrams (size, s):
    a, b = 0, size
    i = 0

    while i <= (len(s)-size):
        yield s[a:b]
        a += 1
        b += 1
        i += 1

s = "the quick red fox jumps over the lazy brown dog"

for x in ngrams(3, s.split()):
    print (x)