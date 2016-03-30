# Module to do hash look ups
# Just as a way of comparison.
# I expect this to be faster but 
# will not be consistent across iterations

# Encode the dictionary
# Key is a hash of the sorted word 
# and value is a set of words
def encoder(a, mapper={}):
    for word in a:
        sortw = sorted(word)
        sortw = "".join(sortw)
        hashedw = hash(sortw)
        words = mapper.get(hashedw, set())
        words.update({word})
        mapper[hashedw] = words
    return mapper


# check the word is in the dictionary

def checker(wrd, mapper):
    srtwrd = sorted(wrd)
    srtwrd = "".join(srtwrd)
    hshwrd = hash(srtwrd)
    results = mapper.get(hshwrd, None)
    return results

# Test code
def  ifExist(x):
    if x:
        return len(x)
    else:
        return 0

a = ['peter', 'paul', 'mary','ramy']
v = encoder(a)
b = ['john', 'james', 'joe', 'mary']
for k in b:
    x = checker(k, v)
    print("{0}: {1} :len {2}".format(k, x, ifExist(x)))



demi = checker("seamus",v)

print ("%s" % demi)




    
