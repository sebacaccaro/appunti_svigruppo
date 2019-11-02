import re
import operator
import functools
# Let's write a module (a pool of functions) that given a quite large text (over than 2000 words) counts how frequent each
# word occurs in the text. In particular the module should provide the function freqs that given a filename and a number
# would return a list of words (with their frequencies) that occur more than the given number; the list is sorted by
# frequency with the higher first.
# The text is read from a file and it is a real text with punctuation (i.e., commas, semicolons, ...) that shouldn't be counted.
#
# Note that words that differ only for the case should be considered the same.


def reader(fileName):
    file = open(fileName)
    for row in file:
        yield splitPunctuation(str.upper(row))
    file.close()


def splitPunctuation(stringToSplit):
    return re.findall(r"[\w']+", stringToSplit)


def countedDictionary():
    counter = {}

    def addNew(word):
        print("ADDNEW -->", word)
        counter[word] = 1

    def increase(word):
        print("INCREASE", word)
        counter[word] = counter[word] + 1

    def apply(word):
        return ((word in counter) and (lambda x: increase(x)) or (lambda x: addNew(x)))

    for word in functools.reduce(operator.concat, list(reader("file.txt"))):
        apply(word)(word)
    return counter


def countWord():
    [functools.reduce(operator.concat, list(reader("file.txt")))]


print(countedDictionary())
