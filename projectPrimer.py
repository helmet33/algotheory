from itertools import permutations
words =[]
with open('wordlist.txt', 'r') as f:
    allwords = f.readlines()
print(f.closed)
for x in allwords:
    x = x.rstrip()
    words.append(x)

words = set(words)

anag = [''.join(p) for p in permutations('andrew', 5)]
anag = set(anag)

result = words.intersection(anag)
print(result)

