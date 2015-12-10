# Read an input file and remove all whitespaces and punctuations in the file
import sys
import string
from string import maketrans
_histogram = {}


def sanitizeWords(word):
    # Use maketrans to substitute each whitespace, punctuation with
    # ' ' and then replace the ' ' with ''
    a = ' '.join(["" for x in range(len(string.whitespace)+1)])
    b = ' '.join(["" for x in range(len(string.punctuation)+1)])
    t1 = maketrans(string.punctuation, b)
    t2 = maketrans(string.whitespace, a)
    word = word.translate(t1)
    word = word.translate(t2)
    word = word.replace(' ', '')
    return word.lower()


def createHistogram(word):
    if word in _histogram:
        _histogram[word] += 1
    else:
        _histogram[word] = 1


def readFile(filename):
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        words = line.split(' ')
        for word in words:
            createHistogram(sanitizeWords(word))

readFile(sys.stdin.readline()[:-1])
print len(_histogram.keys())
