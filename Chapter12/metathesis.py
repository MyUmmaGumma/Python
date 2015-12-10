# Figure out if two anagrams differ by at most 1 swap
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


# Convert to tuple of chars and compare
# Each swap will increment the swap count by 2
def has_one_swap(t1, t2):
    swaps = 0
    for x, y in zip(t1, t2):
        if x != y:
            swaps = swaps + 1
            if swaps > 2:
                return False
    if swaps == 2:
        return True
    return False


def get_metathesis_pairs():
    mpairs = []  # metathesis list of paired words
    for key, value in anagrams.items():
        if len(value) > 1:
            # Iterate over anagrams
            for word1 in value:
                for word2 in value:
                    # Dont compare same words
                    if word1 != word2:
                        # Dont compare pairs already in metathesis list
                        if (word2, word1) not in mpairs:
                            if has_one_swap(word1, word2) is True:
                                mpairs.append((word1, word2))

    print mpairs

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
sort_compare("converse")
sort_compare("conserve")
get_metathesis_pairs()
