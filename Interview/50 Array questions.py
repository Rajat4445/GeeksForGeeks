'''
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


Example 1:

Input: 
N = 3
arr[] = {1,2,3}
Possible Answer: 2
Generated Output: 1
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
If 2 is returned then the generated output will be 1 else 0.
'''
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        return arr.index(max(arr))       # One liner code
      
# Alternative solution
class Solution:   
    def peakElement(self,arr, n):
        # Code here
        max_element = arr[0]
        
        for i in range(n):
            if arr[i]>max_element:
                max_element = arr[i]
                
        return arr.index(max_element)
    


'''
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

Example 1:

Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max =  10000
'''
def getMinMax( a, n):
    
    mini = a[0]
    maxi = a[0]
    
    for i in range(n):
        if a[i]>maxi:
            maxi = a[i]
    
        elif a[i]<mini:          # Using elif ensures that the condition is checked in the same loop
            mini = a[i]
            
    return mini, maxi

'''
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
'''
def reverseWord(s):
    #your code here
    reverse = s[::-1]
    
    return reverse
























