## Have a Thorough look at each and every question ##


'''
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole
string(not individual words), the input
string becomes
much.very.program.this.like.i
'''

    def reverseWords(self,S):
        # code here
        words = S.split('.')
        reverse = words[::-1]
        output = '.'.join(reverse)
        
        return output
    
    
'''
Given a array of N strings, find the longest common prefix among all strings present in the array.

Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek,
         geezer}
Output: gee
Explanation: "gee" is the longest common
prefix in all the given strings.
'''
class Solution:
     
    def longestCommonPrefix(self, arr, n):  # ex: arr = [geeksforgeeks, geeks, geek, geezer]
        if not arr:    # Return -1 if list of strings is empty
            return -1
            
        if n==1:       # Return the first element of the array as output if there is only one element in the array
            return arr[0]
    
        prefix = ""    # Empty string
    
        for group in zip(*arr):         # in first iteration tuple = (g,g,g,g) second = (e,e,e,e) third = (e,e,e,e) and fourth = (e,e,e,k)
            if len(set(group)) == 1:       # if the length of the set of tuple is 1 then only value in tuple gets to the prefix
                prefix += group[0]
            else:                       # Else loop breaks and the prefix is given as the output
                break
    
        return prefix or -1             # IF there is a prefix value return it else give -1 as output
    
    
'''
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
'''


class Solution:
    def romanToDecimal(self, S): 
        # code here
        
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        max_value = 0           # Taking case 'III'
        
        for i in range(len(S)-1, -1, -1): # index 2 (len(s)-1) to index 0 (-1) with step -1
            if roman_values[S[i]] >= max_value:
                result += roman_values[S[i]]
                max_value = roman_values[S[i]]
                
            else:
                result -= roman_values[S[i]]
  
        return result

## Another approach
class Solution:
    def romanToDecimal(self, S):     # Ex: IV and VII
        # code here
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sumint = 0
        for i in range(len(S)):
            if i < len(S) - 1 and roman[S[i]] < roman[S[i+1]]:
                sumint -= roman[S[i]]
            else:
                sumint += roman[S[i]]
               
        return sumint
    
    
'''
Given a list of words followed by two words, the task to find the minimum distance between the given two words in the list of words

Example 1:

Input:
S = { "the", "quick", "brown", "fox", 
     "quick"}
word1 = "the"
word2 = "fox"
Output: 3
Explanation: Minimum distance between the 
words "the" and "fox" is 3
'''


