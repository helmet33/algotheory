from itertools import permutations
import wordGen

# file stuff
words =[]

with open('wordlist.txt', 'r') as f:
    allwords = f.readlines()
print(f.closed)
for x in allwords:
    x = x.rstrip()
    words.append(x)

words = [word for word in words if len(word) <= 9 ]

# Convert list of words to set to ensure no duplicates
words = set(words)

# test word to see if permutations are in set
# start with an empty set and a word
result = set()
i = len('aeestrhar')

# While the set is empty i.e. no anagrams found

while len(result) <= 0 and i > 2:
    anag = [''.join(p) for p in permutations('aeestrhar', i)]
    anag = set(anag)

    result = words.intersection(anag)
    i = i - 1

print(result)

#TEST CODE - for import testing ( a known known)
lister = wordGen.getLetters()

print(lister)
print(len(lister))
#END TEST CODE
# Test


