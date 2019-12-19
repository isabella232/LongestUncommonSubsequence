import math 	# allows for use of sorting function

def IsSubsequence(str1, str2, m, n): #returns true is string1 is a subsequence of string2
	
	# if string length is 0
  
    # If last characters of two strings are matching 
  
    # If last characters are not matching 
  
def LUS(arr): 
  
  	# Convert array to set. A set removes all duplicate elements so if after converting, the length is 1
  	# it means that all the strings were equal to each other.

	
	# sorting strings by length (descending order)

	
	# checking a string in array
	
	
		# checking next string in array and if its a subsequence of any other string
		
					
		
		# if the string is a subsequence of another string, move on to the next longest string in the array
		
		
	# otherwise return that there is no longest uncommon subsequence
	
arr = ["aaabbb", "aaabbb", "a", "abc"]
print (LUS(arr))
