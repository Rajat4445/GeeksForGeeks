'''
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 

Example:
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

        max_element = arr[0]     # Taking first element of array as max
        
        for i in range(len(arr)):       # iterating thorugh each element in array to get max_element out of the given array
            if arr[i]>max_element:
                max_element = arr[i]
            else:
                pass
            
        return arr.index(max_element)     # Fetching the index of max_element (first occurence)
    
    
'''
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

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
    
        elif a[i]<mini:
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
    reverse = ''
    n = len(s)
    
    for i in range(n):
        reverse += s[n-i-1]
    
    return reverse

'''
Given a random set of numbers, Print them in sorted order.

Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: {1, 2, 3, 5}
Explanation: After sorting array will 
be like {1, 2, 3, 5}.
'''
class Solution:
    def sortArr(self, arr, n):      
        
        for i in range(n):
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]      # (Bubble Sort)
                    
        return arr
    
