# My permutations, from a conversation at 
# http://stackoverflow.com/questions/8683092/calculating-combinations-of-length-k-from-a-list-of-length-n-using-recursion

def permute(word, n):
	# if we reach zero return empty list
    if n==0: yield []
    else:
    	# traverse word length
        for i in range(len(word)):
        	# traverse rest of word and recur
            for combo in permute(word[i+1:],n-1):
                yield [word[i]]+combo


