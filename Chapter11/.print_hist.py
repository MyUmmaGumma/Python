def histogram(s):
    d = dict()
    print s
    for c in s:
        print c
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def print_hist(d):
    a = d.keys()
    a.sort()
    for key in a:
        print key + str(d[key])

a = histogram("This is a sentence with many words")
import pprint
pprint.pprint(a)
print_hist(a)
