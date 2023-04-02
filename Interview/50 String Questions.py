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

'''
