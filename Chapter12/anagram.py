# Read a bunch of words and classify anagrams in them
anagrams = {}


# Uses the DSU pattern to store tuple of letters per  word as key in dictionary
def sort_compare(word):
    tword = tuple(word)

    t = []
    for l in tword:
        t.append((l, len(l)))

    t.sort()
    lres = []

    for l, let in t:
        lres.append(l)

    res = tuple(lres)

    if res in anagrams:
        anagrams[res].append(word)
    else:
        anagrams[res] = [word]


# Prints the value of the dictionary which is the list of anagrams
def print_anagrams():
    for key, value in anagrams.items():
        print value


# Prints the largest set of anagrams first and so on
def print_sorted_anagrams():
    sort = []
    for key, value in anagrams.items():
        sort.append((len(value), value))

    sort.sort(reverse=True)

    for l, lis in sort:
        print lis


sort_compare("basic")
sort_compare("adamant")
sort_compare("deltas")
sort_compare("salted")
sort_compare("lasted")
sort_compare("til")
sort_compare("lit")
sort_compare("smelters")
sort_compare("termless")
sort_compare("staled")
print_sorted_anagrams()
