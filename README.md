### Garrett Jordan
##### G00305145
----
##### Module: Theory of Algorithms
##### Course: BSc.(Hons) Software Development - Year 4
##### Lecturer: Dr. Ian McLoughlin
----
##### GIT REPOSITORY FOR THIS PROJECT: https://github.com/helmet33/algotheory
##### All scripts written and run using Python 3.51 (Anaconda version)
----
# Countdown Letters Game Solver



## Introduction
Countdown is a word and number puzzle game on afternoon TV. It is particularly loved by students, the unemployed and the retired.  Another version called Two Cats do Countdown is a more adult version screened after the watershed.
I am familiar with the show Countdown and particularly the show Two Cats do Countdown. I did however reference the [Countdown wiki][1] for a breakdown of the rules and permissible words.


## Rules
The following rules were adhered to:
1. A selection of 9 letters is used from which to find words.
2. The selection must contain at least 3 vowels.
3. The selection must include at least 4 consonants.
4. The selection may include more then one instance of the same letter.
5. The word created from the selection can use any combination of the selection  without replacement i.e. each individual letter can be used only once.
6. The word must be included in the word list as generated.
7. No proper nouns or apostrophes allowed.

Additionally:
* I use the scrabble distribution of letters. This ensures that the most common letters in the English language occur more often then those rarely used. This means that there is a pool of 98 letters from which to generate the 9 letter selection. The inclusion of a weighted letters pool means that there is rarely a case of 3 letter words only.
* I decided to make the implementation more like the game in that it returns when  the longest word or collection of words is found. If it finds 2 * 8 letter words it returns those words and stops searching for  smaller words.



## Words list
My words lists is in the files wordlist.txt and wordslistMoby.txt in the GitHub repository.
I got my words list from the Linux Moby list from this  [website][2] and from a second year project in Data Structures and Algorithms. The Moby dictionary contains 354934 words and the wordlist dictionary contains 69905 words. Both dictionaries provide more words than the 3000 available at the Oxford English Dictionary site.

## Approach
I am familiar with the show Countdown and initially concentrated not on the rules but on simply finding permutations of given letters in a list of known words.
I initially wanted to examine the efficiency of some of the Python built-in data structures and functions. Specifically I wanted to investigate the use of the Python native implementation of the Set data structure. If a set 𝐴 contains all known words and another smaller set 𝐵 contains all permutations of a given set of letters then then 𝐴 ∩ 𝐵 is the set containing permutations that are actual words.
I initially used the itertools module to return the list of permutations for given input. This library appears to be the de facto standard for doing work with iterators in Python. I was not content to just use it however, and researched the source code and method used by itertools' permutations module, which I discuss when referencing the iterToolsSource.py file below.

Although the Set approach and itertools work I decided to research using combinations instead of permutations and this is the solution as implemented. I decided to sort words and store each word in a Dict with the hash of the sorted word as key and word added to a set as the value. Combinations were then sorted, hashed and checked against the dictionary.

## Python scripts
### projectPrimer.py
My main script is in the files [projectPrimer.py](https://github.com/helmet33/algotheory/blob/master/projectPrimer.py) in my GitHub repository. The file takes a Set as returned from preprocessing my word lists:

```python
words = fileStuff.getDictionary()
hashD = dict(hasher.encoder(words))
```

I then check if the hash of each combination of decreasing length is contained in the Dict and return when found. This version doesn't use itertools but uses myPerms.py to return combinations:

```python
while len(result) <= 0 and i > 2:
    anag = [''.join(p) for p in myPerms.permute(inp, i)]
    anag = set(anag)
    for wrd in anag:
        words = hasher.checker(wrd, hashD)
        if words:
            result = words        
    i = i - 1
```
I have left the original set method in the file. It has however been commented out. The set method was as follows and uses the itertools library:

```python
    while len(result) <= 0 and i > 2:
        anag = [''.join(p) for p in permutations(inp, i)]
        anag = set(anag)
        # check if any anagrams in Set of words
        result = words.intersection(anag)
        i = i - 1
```
### myPerms.py
I decided to research combinations instead of the itertools permutations module. The method permute takes a list and a number, the number is the length of required unique combination. Combinations are efficient when we are sorting the output. The method recurs over the word combining the first letter with combinations of the following letters. Once the first letter is combined with the following letters it is no longer needed and the next letter is combined with the remaining letters. This happens until the end of the word. This method is discussed in depth in this [Stack Overflow post][3]:
```python
def permute(word, n):
	# if we reach zero return empty list
    if n==0: yield []
    else:
    	# traverse word length
        for i in range(len(word)):
        	# traverse rest of word and recur
            for combo in permute(word[i+1:],n-1):
                yield [word[i]]+combo
```

### hasher.py
The hasher.py file as discussed in preprocessing is also used for look up. The method used is checker() which takes in a word and the Dict. It sorts the word and looks it up on the map. It returns a set of words if it exists or None if it isn't in the map. None allows the script to continue without a key lookup exception.
```python
def checker(wrd, mapper):
    srtwrd = sorted(wrd)
    srtwrd = "".join(srtwrd)
    hshwrd = hash(srtwrd)
    results = mapper.get(hshwrd, None)
    return results
```
## Preprocessing
Before I check for matches I make use of two files during preprocessing:
1. fileStuff.py - reads in and processes words from my selected word lists. Cleans up white space and returns a set of unique words. Proper nouns and words over 9 letters are excluded  at this stage.
2. wordGen.py - creates a group of 9 letters as outlined in the rules section. Uses the scrabble distribution of letters as a pool and selects 3 vowels, 4 consonants and 2 other random letters. This returns a list from which we will endeavor to find legal words.
3. hasher.py - creates a hash keyed Python Dict for my 2nd and final solution.

### fileStuff.py
Reads a flies into a set. It contains 2 methods that combine to return a Set of words. List comprehension is used, as follows, to ensure that the words are legal:
```python
# Words are less then or equal to 9 and uncapitalised
    words = [word for word in words if len(word) <= 9 and words[0].islower()]
    # Convert list of words to set to ensure no duplicates
    words = set(words)
```
The word is checked to be 9 letters or less and not a proper noun i.e. not capitalized. This reduces the search space and processing in later steps as it ensures that the words are legal.

### wordGen.py
In the wordGen.py file I create two lists: vowels and consonants. I then use a method to append letters to a list based on the [scrabble distribution][4] of letters:
```python
letters= list()
    letters.extend(list('e' * 12))
    letters.extend(['a', 'i'] * 9)
```

The genWord() method then loops through the vowels and consonants to fulfill the rules. An additional to random characters are appended to complete the selection. As letters are selected they are removed from the letters pool. The nine letter selection is then returned.

### hasher.py
This file looks after creating the hash Dict and looking up words. It is an amended version of the algorithms solution from class. I encode a list of words by using the encode() method. This message takes in a list and for each item in the list  sorts it, hashes it, uses the hash as the key and the word as value. This allows for very quick look ups.
```python
def encoder(a, mapper={}):
    for word in a:
        sortw = sorted(word)
        sortw = "".join(sortw)
        hashedw = hash(sortw)
        words = mapper.get(hashedw, set())
        words.update({word})
        mapper[hashedw] = words
    return mapper
```
## itertools

I initially used itertools permutations module to find all permutations. I have included a file iterToolsSource.py which I took from the itertools documentation. I went through the file and printed output at various stages. I concluded that the library uses [Permutation Cycles][5] to generate permutations.  

## Efficiency
The decision to use combinations instead of permutations coupled with the use of a hash look up on the Dict file really improved performance as is evidenced from the timings in Results section below.

The formula for calculating combinations is:

 C(n,r) = n! / r! (n - r)!
 
 The formula for calculating permutations is:
 
 P(n,r) = n! / (n - r)!
 
where n is the number of elements and r is the subset size. In 9 letter words alone the following calculations emphasis the improvements:
 
 P(9,9)= 362880
 
 C(9,9)= 1
 
 Thats 362879 less lookups by using combinations.

 Using a hashed key in the Dict allows for a constant time O(1) lookup of the hashed value of a word. The set.intersection(set2) method needs to check each value in the smaller set exists in the larger set.

## Running and Results
All scripts are written in Python 3. Testing was done via IPython.

Running the projectPrimer.py file from the directory using Ipython:
```bash
run projectPrimer
```
or from terminal (substitute python for your python 3 command):
```bash
python projectPrimer.py
```
These will result in the letters selection and the largest results printed to screen as shown:
```bash
In [3]: run projectPrimer.py
['u', 'f', 'i', 'c', 'i', 'w', 'v', 'e', 'j']
{'juice'}
```

I created a timeTest.py file which I used to time the individual methods used which can be run as follows (including results):

getResults() checks combinations in Dict:
```bash
python -mtimeit -s'import timeTest' 'timeTest.getResult()'
100 loops, best of 3: 1.95 msec per loop
python -mtimeit -s'import timeTest' 'timeTest.getResult()'
1000 loops, best of 3: 1.99 msec per loop
python -mtimeit -s'import timeTest' 'timeTest.getResult()'
1000 loops, best of 3: 1.98 msec per loop
```

getResultsSet() checks permutations in set:
```bash
python -mtimeit -s'import timeTest' 'timeTest.getResultSet()'
10 loops, best of 3: 476 msec per loop
python -mtimeit -s'import timeTest' 'timeTest.getResultSet()'
10 loops, best of 3: 471 msec per loop
python -mtimeit -s'import timeTest' 'timeTest.getResultSet()'
10 loops, best of 3: 473 msec per loop
```

getResultsHash() checks permutations in Dict:
```bash
python -mtimeit -s'import timeTest' 'timeTest.getResultHash()'
10 loops, best of 3: 1.5 sec per loop
python -mtimeit -s'import timeTest' 'timeTest.getResultHash()'
10 loops, best of 3: 1.5 sec per loop
python -mtimeit -s'import timeTest' 'timeTest.getResultHash()'
10 loops, best of 3: 1.52 sec per loop
```
The results above show significant differences. The getResult() method is reflective of the one used in my main script, due to the fact it uses combinations the overhead of doing hashing is negligible and the results are very quick. 
The getResultSet() and getResultHash() methods both use itertools permutations and the Set method proves quicker by some margin. The hashing overhead with many permutations seems to be the main factor here. All the above were run using the input 'esimezdat' which was generated using the wordGen module.

I also ran timing tests on both the iterToolsSource.py and myPerms.py using the following methods in timeTest.py:

iterpermutes() returns permutations of 'slovenia':
```bash
python -mtimeit -s'import timeTest' 'timeTest.iterpermutes()'
10 loops, best of 3: 283 msec per loop
python -mtimeit -s'import timeTest' 'timeTest.iterpermutes()'
10 loops, best of 3: 279 msec per loop
python -mtimeit -s'import timeTest' 'timeTest.iterpermutes()'
10 loops, best of 3: 289 msec per loop
```

mypermutes() returns combinations of 'slovenia':
```bash
python -mtimeit -s'import timeTest' 'timeTest.mypermutes()'
10000 loops, best of 3: 195 usec per loop
python -mtimeit -s'import timeTest' 'timeTest.mypermutes()'
10000 loops, best of 3: 200 usec per loop
python -mtimeit -s'import timeTest' 'timeTest.mypermutes()'
10000 loops, best of 3: 198 usec per loop
```
This proves, without doubt, that the combinations method is far quicker then using permutations.

In conclusion using combinations instead of permutation and using a hash Dict for storage and lookup is the most efficient method I have come across. The coupling use of combinations means that the additional overhead of hashing is redundant due to the significant reduction in items to be hashed.




## References
I made use of the Python 3.5 documentation for Sets, Lists and Dicts. I also reference the itertools library. All other references above are linked to source and are visible when viewing the raw markdown.

[1]: http://wiki.apterous.org/Main_Page

[2]: http://www.clres.com/dict.html

[3]:  http://stackoverflow.com/questions/8683092/calculating-combinations-of-length-k-from-a-list-of-length-n-using-recursion

[4]: https://en.wikipedia.org/wiki/Scrabble_letter_distributions#English

[5]: https://en.wikipedia.org/wiki/Cyclic_permutation

[6]: https://docs.python.org/3/library/stdtypes.html

[7]: https://docs.python.org/3/library/itertools.html


