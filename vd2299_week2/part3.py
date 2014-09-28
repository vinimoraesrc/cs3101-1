def query():
    """Returns two dictionaries as specified in the problem, item (a).

    - zip_to_tuple stands for the dict mapping zip codes to info tuples
    - town_to_zip stands for the dict mapping town to sets of zip codes

    Iterates over the lines in the markets.tsv file, forming a tuple
    with each farmers market's infos and appending it to a list.
    The function then proceeds to create the appropriate mapping in
    the dictionaries.

    Note that there are some data missing in the file, such as in lines
    3510 and 3511, which this function does not treat as special cases,
    handling them normally, thus the user may notice some '' values in
    the return of the dictionaries.
    """

    f = open('markets.tsv', 'r',  encoding="iso-8859-1")

    zip_to_tuple = {}
    town_to_zip = {}

    x = 0
    for l in f:
        t = tuple(l.strip().split('\t'))

        zip_code = t[4]
        town = t[3]

        if zip_code not in zip_to_tuple:
            zip_to_tuple[zip_code] = [t]
        else:
            zip_to_tuple[zip_code] += [t]

        if town not in town_to_zip:
            town_to_zip[town] = [zip_code]
        else:
            if zip_code not in town_to_zip[town]:
                town_to_zip[town] += [zip_code]

        # Some queries, such as '', may present encoding errors, so I 
        # used this workaround to limit the number of lines read while
        # testing my program (line 53 has an encoding error).

        #x += 1
        #if x == 50:
        #    break

    f.close()

    return zip_to_tuple, town_to_zip

def format(state, name, address, town, zip):
    """Returns a formatted string as specified in item (b).

    As it was said in the query function, there are some markets with
    missing data in the file and these are handled normally. Therefore,
    there may be some blank lines in the return of this function if 
    there is indeed missing information.
    """
    formatted_str = "{0}\n{1}\n{2}, {3} {4}\n".format(name, address, town, state, zip)

    return formatted_str

def database():
    """Repeatedly searchs for farmers markets based on user's input.

    If the input contains only numbers, it is considered to be a zip.
    If the input also contains letters, it is considered to be a town.

    The function then checks if the database contains the input, 
    telling the user if it does not. If it does contain the data, 
    the requested information is printed as specified.

    Please note encoding errors mentioned in the documentation of 
    previous functions.
    """

    zip_to_tuple, town_to_zip = query()

    l = ''

    while l != quit:

        l = input("Type in a zip code, a town name, or quit:\n")

        if l == 'quit':
            break

        elif l.isdigit(): # zip code

            if l in zip_to_tuple:
                for i in zip_to_tuple[l]:
                    try:
                        print (format(i[0], i[1], i[2], i[3], i[4]))
                    except:
                        print ("Cannot print line due to enconding problems.\n")

            else:
                print ("Zip code {0} is not on the database.\n".format(l))

        else: # town name

            if l in town_to_zip:

                for i in town_to_zip[l]:
                    for j in zip_to_tuple[i]:
                        try:
                            print (format(j[0], j[1], j[2], j[3], j[4]))
                        except:
                            print ("Cannot print line due to enconding problems.\n")

            else:
                print ("Town {0} is not on the database.\n".format(l))

# Unit tests for item (a)
#print (zip_to_tuple['49770'])
#print (town_to_zip['Albertville'])

# Unit tests for item (b)
#for i in town_to_zip['Albertville']:
#    tmp = zip_to_tuple[i]
#    print (format(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4]))

database()