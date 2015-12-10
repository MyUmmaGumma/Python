# Print the frequency of letters in decreasing order of frequency in a string

import sys
inputstr = sys.stdin.readline()[:-1]


# Uses the decorate-sort-undecorate pattern!
def sort_by_frequency(d):
    t = []
    for key, value in d.items():
        t.append((value, key))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res

newdict = {}
t = tuple(inputstr)
for letter in t:
    if letter in newdict:
        newdict[letter] = newdict[letter]+1
    else:
        newdict[letter] = 1

l = sort_by_frequency(newdict)

print l
