from itertools import permutations
words =[]
with open('wordlist.txt', 'r') as f:
    allwords = f.readlines()
print(f.closed)
for x in allwords:
    x = x.rstrip()
    words.append(x)

words = set(words)

result = set()
i = len('lephnat')
while len(result) <= 0 and i > 2:
    anag = [''.join(p) for p in permutations('lephnat', i)]
    anag = set(anag)

    result = words.intersection(anag)
    i = i - 1

print(result)

