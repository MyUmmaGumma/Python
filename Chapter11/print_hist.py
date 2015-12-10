# Print the histogram of letters in a sentence in sorted order.


def histogram(s):
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def print_hist(d):
    a = d.keys()
    a.sort()
    for key in a:
        print key + " " + str(d[key])

a = histogram("This is a sentence with many words")
print_hist(a)
