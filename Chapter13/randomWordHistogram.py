# Choose a word from a histogram that is random with equal probability weights
import random
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
    if word is '':
        return
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


# Create a list containing cumulative word frequencies of the histogram
def cumulativeSum():
    cumulative = []
    wordList = []
    runningSum = 0
    for key, value in _histogram.items():
        runningSum += value
        cumulative.append(runningSum)
        wordList.append(key)
    # Generate a random number
    for i in range(0, 10):
        rnum = random.randrange(0, cumulative[-1])
        a, b = binarySearch(rnum, cumulative, 0, len(cumulative))
        print "Random word: " + wordList[a]


# Search for 'search' in list l
def binarySearch(search, l, low, high):
    mid = (low + high) / 2
    if mid == low + 1 or mid == high - 1 or l[mid] == search:
        if search < l[mid]:
            print "Between " + str(mid-1) + " " + str(mid)
            a, b = mid-1, mid
        elif search > l[mid]:
            print "Between " + str(mid) + " " + str(mid+1)
            a, b = mid, mid + 1
        else:
            print "Index is " + str(mid)
            a, b = mid, mid
        return a, b
    if search > l[mid]:
        return binarySearch(search, l, mid+1, high)
    elif search < l[mid]:
        return binarySearch(search, l, low, mid-1)

readFile(sys.stdin.readline()[:-1])
cumulativeSum()
