import math 

def IsSubsequence(str1, str2, m, n): #returns true is string1 is a subsequence of string2
 
    if m == 0:    return True
    if n == 0:    return False
  
    # If last characters of two strings are matching 
    if str1[m-1] == str2[n-1]: 
        return IsSubsequence(str1, str2, m-1, n-1) 
  
    # If last characters are not matching 
    return IsSubsequence(str1, str2, m, n-1) 
  
def LUS(arr): 
  
  	# Converting array to set. A set removes all duplicate elements so if after converting, the length is 1
  	# it means that all the strings were equal to each other.
	if len(set(arr)) == 1:
		return -1

	arr.sort(key=len, reverse=True) # sorting strings by length (descending order)

	for str1 in arr:
		subflag = False
		equal = 0

		for str2 in arr: # checking if the string is a subsequence of any other string
			if str1 == str2:
				equal = equal + 1
			else:
				if IsSubsequence(str1,str2,len(str1),len(str2)):
					subflag = True	
					
		# if the string is a subsequence of another string
		# move on to the next longest string in the array
		if subflag == True or equal == 2: 
			continue
		else:
			return len(str1)
	return -1

arr = ["aaabbb", "aaabbb", "a", "abc"]
print (LUS(arr))
