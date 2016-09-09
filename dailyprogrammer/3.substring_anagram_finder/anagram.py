
#finds all permutations of pattern in string in O(str) time

len_ASCII = 128 #length of non extended ASCII table

def anagram(pattern, string):

	pattern_len = len(pattern)
	string_len = len(string)

	#store indices of anagrams 
	anagrams = []

	pattern_arr = [0] * len_ASCII
	string_arr = [0] * len_ASCII

	#Use ASCII value as index of array
	for indx, char in enumerate(pattern):
		#store pattern in pattern array
		pattern_arr[ord(char)] += ord(char)	
		#store pattern_len characters from string into string array	
		string_arr[ord(string[indx])] += ord(string[indx])
	#if arrays are equal, we have an anagram
	if pattern_arr == string_arr:
		anagrams = [0]

	#pop first character off string array and add new character
	#repeat array comparisons until the end
	for indx in range(pattern_len, string_len ):
		begin_char = string[indx - pattern_len]
		end_char = string[indx]

		string_arr[ord(begin_char)] -= ord(begin_char)
		string_arr[ord(end_char)] += ord(end_char)

		if pattern_arr == string_arr:
			anagrams.append(indx - pattern_len + 1)

	print anagrams

anagram("abc","cbadabcaabc")


