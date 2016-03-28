# file stuff
dictionary = set()
def genDictionary(wFile):
    words = []
    with open(wFile, 'r') as f:
        allwords = f.readlines()
    for x in allwords:
        x = x.rstrip()
        words.append(x)
    # Words are less then or equal to 9 and uncapitalised
    words = [word for word in words if len(word) <= 9 and words[0].islower()]
    # Convert list of words to set to ensure no duplicates
    words = set(words)
    return words

def getDictionary():
    if (len(dictionary) <= 0):
        dictionary.update(genDictionary('wordlist.txt'))
    return dictionary
