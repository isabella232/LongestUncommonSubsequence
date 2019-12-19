
## Part 1 - Longest Uncommon Subsequence ##

def LUS(strA, strB):
	# If the strings are the same, clearly subsequences of each other
	if (strA == strB):
		return -1;
	else:
		# Will return the length of string that is the longest, or of both 
		# if the same length: both mean an uncommon subsequence was found.
		return max(len(strA), len(strB));	

strA = raw_input("1: ")
strB = raw_input("2: ")

print(LUS(strA, strB));



