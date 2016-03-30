from itertools import permutations
import wordGen
import fileStuff
import hasher
import timeit
import iterToolsSource
import myPerms



#Generate the dictionary these are checked from
# The modules individually
words = fileStuff.getDictionary()
hashDict = hasher.encoder(words)

# for timing

def  generateHashDict():
    hashDict = hasher.encoder(words)


# test word to see if permutations are in set
# start with an empty set and a word
# for the purposes of timing script
# input will be kept constant as the the generation 
# method is not undertest. I used the word generator
# in word gen to generate these letters.
def getResult():
    result = set()
    inp = 'esimezdat'
    #print(inp)
    i = len(inp)

    # While the set is empty i.e. no anagrams found
    while len(result) <= 0 and i > 2:
        anag = [''.join(p) for p in myPerms.permute(inp, i)]
        anag = set(anag)
        for wrd in anag:
            words = hasher.checker(wrd, hashDict)
            if words:
                result = words

        
        i = i - 1

    
    return result

def getResultSet():
    result = set()
    inp = 'esimezdat'
    #print(inp)
    i = len(inp)

    # While the set is empty i.e. no anagrams found

    while len(result) <= 0 and i > 2:
        anag = [''.join(p) for p in permutations(inp, i)]
        anag = set(anag)

        result = words.intersection(anag)
        i = i - 1

    return result

def getResultHash():
    result = set()
    inp = 'esimezdat'
    i = len(inp)

    # While the set is empty i.e. no anagrams found


    while len(result) <= 0 and i > 2:
        anag = [''.join(p) for p in permutations(inp, i)]
        anag = set(anag)
        for wrd in anag:
            words = hasher.checker(wrd, hashDict)
            if words:
                result = words

        
        i = i - 1

    return result

def iterpermutes():
    s = sorted('slovenia')
    per = [''.join(p) for p in iterToolsSource.permutations(s)]
    return per    

def mypermutes():

    s = list('slovenia')
    gj = list()
    gj = [''.join(p) for p in myPerms.permute(s, 3)]

    #for perm in myPerms.permute(s, 3):
    #    gj.append(sorted(perm))
    return gj

# min(timeit.Timer(getResult).repeat(repeat=3, number=10))

#print(getResult())
#iters = iterpermutes('james')
#myperms =  mypermutes('james')
#print(myperms)


#TEST CODE - for import testing ( a known known)
#lister = wordGen.getLetters()

#print(lister)
#print(len(lister))

#twist = wordGen.genWord()
#print(twist)

#END TEST CODE
# Test



