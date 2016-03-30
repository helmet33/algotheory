from itertools import permutations
import wordGen
import fileStuff
import myPerms
import hasher



# file stuff
#words =[]
#
#with open('wordlist.txt', 'r') as f:
#    allwords = f.readlines()
#print(f.closed)
#for x in allwords:
#    x = x.rstrip()
#    words.append(x)
#
#words = [word for word in words if len(word) <= 9 ]
#
# Convert list of words to set to ensure no duplicates

#words = set(words)
words = fileStuff.getDictionary()
hashD = dict(hasher.encoder(words))


# Set method
# test word to see if permutations are in set
# start with an empty set and a word
result = set()
inp = wordGen.genWord()
print(inp)
i = len(inp)



#set method
#
#While the set is empty i.e. no anagrams found


#    while len(result) <= 0 and i > 2:
#        anag = [''.join(p) for p in permutations(inp, i)]
#        anag = set(anag)
#    
#        result = words.intersection(anag)
#        i = i - 1



# Hash method



while len(result) <= 0 and i > 2:
    anag = [''.join(p) for p in myPerms.permute(inp, i)]
    anag = set(anag)
    for wrd in anag:
        words = hasher.checker(wrd, hashD)
        if words:
            result = words

        
    i = i - 1
  
print(result)



#TEST CODE - for import testing ( a known known)
#lister = wordGen.getLetters()

#print(lister)
#print(len(lister))

#twist = wordGen.genWord()
#print(twist)

#END TEST CODE
# Test


