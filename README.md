### Garrett Jordan
#### G00305145

#### GIT REPOSITORY FOR THIS PROJECT: https://github.com/helmet33/algotheory

# Countdown Letters Game Solver



## Introduction
I am familiar with the show Countdown and particularly the show Two Cats do Countdown. I did however reference the COUNTDOWN wiki for a breakdown of the rules and permissible words.
Google gave me two relevant results on the first page, these are [Cool Project name][2] and [Cool Solver][3].

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
* I decided to make the implementation more like the game in that it returns when  the longest word or collection of words is found. If it finds 2 8 letter words it returns those words and stops searching for  smaller words.



## Words list
My words lists is in the files wordlist.txt and wordslistMoby.txt in the GitHub repository.
I got my words list from the Linux Moby list from this  [website] and from a second year project in Data Structures and Algorithms. The Moby dictionary contains 354934 words and the wordlist dictionary contains 69905 words. Both dictionaries provide more words then the 3000 available at the Oxford English Dictionary site.

## Initial approach
I am familiar with the show Countdown and initially concentrated not on the rules but on simply finding permutations of given letters in a list of know words.
I initially wanted to examine out the efficiency of some of the Python built in data structures and functions. Specifically I wanted to investigate the use of the Python native implementation of the  Set data structure. If a set 𝐴 contains all known words and another smaller set 𝐵 contains all permutations of a given set of letters then then 𝐴 ∩ 𝐵 is the set containing permutations that are actual words.
I initially used the itertools module to return the list of permutations for given input. This library is appears to be the de facto standard for doing work with iterables in Python. I was not content to just use it however, and researched the source code and method used by itertools' permutations module, which I discuss when referencing the iterToolsSource.py file below.

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
I decided to research combinations instead of the itertools permutations module. The method permute takes a list and a number the number is the length of required unique combination. Combinations are efficient when we are sorting the output. The method recurs over the word combining the first letter with combinations of the following letters. Once the first letter is combined with the following letters it is no longer needed and the next letter is combined with the remaining letters. This happens until the end of the word. This method is discussed in depth in this [Stack Overflow post](2):
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
## Preprocessing
Before I check for matches I make use of two files during preprocessing:
1. fileStuff.py - reads in and processes words from my selected word lists. Cleans up white space and returns a set of unique words. Proper nouns and words over 9 letters are excluded  at this stage.
2. wordGen.py - Creates a group of 9 letters as outlined in the rules section. Uses the scrabble distribution of letters as a pool and selects 3 vowels, 4 consonants and 2 other random letters. This returns a list from which we will endeavor to find legal words.
3. hasher.py - creates a hash keyed Python Dict for my 2nd and final solution.

### fileStuff.py
Reads a flies in to a set. It contains 2 methods that combine to return a Set of words. List comprehension is used, as follows, to ensure that the words are legal:
```python
# Words are less then or equal to 9 and uncapitalised
    words = [word for word in words if len(word) <= 9 and words[0].islower()]
    # Convert list of words to set to ensure no duplicates
    words = set(words)
```
The word is checked to be 9 letters or less and not a proper noun i.e. not capitalized. This reduces the search space and processing in later steps as it ensures that the words are legal.

### wordGen.py
In the wordGen.py file I create to lists; vowels and consonants. I then use a method to append letters to a list based on the [scrabble distribution](3) of letters:
```python
letters= list()
    letters.extend(list('e' * 12))
    letters.extend(['a', 'i'] * 9)
```

The genWord() method then loops through the vowels and consonants to fulfill the rules. An additional to random characters are appended to complete the selection. As letters are selected they are removed from the letters pool. The nine letter selection is then returned.


## Efficiency
Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

## Results
My script runs very quickly, and certainly within the 30 seconds allowed in the Countdown letters game.


## References
[1]: http://www.clres.com/dict.html

[2]:  http://stackoverflow.com/questions/8683092/calculating-combinations-of-length-k-from-a-list-of-length-n-using-recursion

[3]: https://en.wikipedia.org/wiki/Scrabble_letter_distributions#English

