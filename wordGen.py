import random

# All vowels and all consanants available for selection to set initial minimum requirements. Letters will initially be selected from these two lists as per rules and when selected removed from letters pool.

vowels = ( 'a', 'e', 'i', 'o', 'u' )
consonants = ( 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')


# Use the scrabble English distribution of letters for the letters.
# Initial empty list and then append single letters or extend with list of letters as
# warranted
# Scrabble Distribution: https://en.wikipedia.org/wiki/Scrabble_letter_distributions#English
# Excluded blank tiles as illegal in this context (Countdown) total 98 letters

# letters = list()

def genList():
    letters= list()
    letters.extend(list('e' * 12))
    letters.extend(['a', 'i'] * 9)
    letters.extend(list('o' * 8))
    letters.extend(['n','r','t'] * 6)
    letters.extend(['l', 's', 'u', 'd']* 4)
    letters.extend(list('g' * 3))
    letters.extend(['b' , 'c', 'm', 'p', 'f', 'h', 'v', 'w', 'y']* 2)
    letters.extend(['k', 'j', 'x', 'q', 'z'])
    return letters

# TODO
# Select vowels and consonants, remove from letters pool shuffle and pop remaining letters return word. 
# Split to methods and import to runner
# random.shuffle(letters)

lettersG = genList()
# TEST CODE - test method for import - a known known
def getLetters():
    # Neccessary to copy list to avoid it emptying and also 
    # to avoid regeneration
    letters = list(lettersG)
    return letters

def getConsnants(letPool):
    letterOK = False
    c = ''
    while letterOK == False:
        c = random.choice(consonants)
        if  letPool.count(c)>0:
            letterOK = True
    return c

def genWord():
    lets = list(lettersG)
    word = []
    for i in range (0,3):
        v = random.choice(vowels)
        c = getConsnants(lets)
        #c = random.choice(consonants)
        
        word.extend([v, c])
        lets.remove(v)
        lets.remove(c)

    c = getConsnants(lets)
    word.append(c)
    lets.remove(c)
    for i in range (0,2):
        l = random.choice(lets)
        word.append(l)
    return word



        
# END TEST CODE
