# This code will change the casing of word/password not including numbers.
# Enter the text you'd like to change into the "remove me" and run the code.
# The output should give you all possible passwords/words
 
def permute(inp): 
	n = len(inp) 
 
	mx = 1 << n 

	inp = inp.lower() 
	
	for i in range(mx): 
		combination = [k for k in inp] 
		for j in range(n): 
			if (((i >> j) & 1) == 1): 
				combination[j] = inp[j].upper() 

		temp = "" 
		for i in combination: 
			temp += i 
		print temp, 
		
    #EditText \/
permute("remove me") 

# This code is contributed by Nathan Dickinson
