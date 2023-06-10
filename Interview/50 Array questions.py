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
def reverseWord(s):              # Shortest way
    #your code here
    reverse = s[::-1]
    
    return reverse

# USing for loop
def reverseWord(s):
    #your code here
    reverse = ''              # empty string
    
    for i in range(len(s)):     # without using indexing
        reverse += s[len(s)-i-1]
        
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
        #code here
        copy = arr
        output = []
        
        while len(copy)>0:                        # !! Time limit exceeds here !! Very slow
            output.append(min(copy))
            copy.remove(min(copy))
            
        return output

# sorted(arr) is the best method which uses minimum time.
    
'''
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.
'''

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        s_array = sorted(arr)
        
        return s_array[k-1]     # Brute force approach

class Solution:
    def kthSmallest(self,arr, l, r, k):
        
        copy = arr.copy()
        s_array = []
        
        while len(copy) != 0:               # Exceeds time limit but does the job

            s_array.append(min(copy))
            copy.remove(min(copy))
            
        return s_array[k-1]

'''
Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.
Example 1:

Input:
N = 5
vector = {1, 1, 1, 1, 1}
X = 1
Output: 
5
Explanation: Frequency of 1 is 5.
'''

def findFrequency (arr, n, x):
    # Your Code Here
    
    return arr.count(x)        # Brute force

def findFrequency (arr, n, x):
    # Your Code Here
    
    count = {}         # Using dictionary approach
    
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    return count[x]

def findFrequency (arr, n, x):
    # Your Code Here
    
    count = 0      # Counter approach
    
    for i in arr:
        if i == x:
            count += 1
            
    return count


'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
'''
class Solution:
    def sort012(self,arr,n):
        
        count_0 = arr.count(0)
        count_1 = arr.count(1)
        count_2 = arr.count(2)

    # Update the array with the sorted values, this is faster because instead of making a new array, we are modifying the existing
        for i in range(count_0):
            arr[i] = 0
        for i in range(count_0, count_0 + count_1):
            arr[i] = 1
        for i in range(count_0 + count_1, len(arr)):
            arr[i] = 2

        return arr

'''
Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:

Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5
'''
class Solution:
    def segregateElements(self, arr, n):
        
        j = 0
        for i in range(n):         # Have a closer look at the loop and values of i and j properly
            if arr[i]<0:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                j += 1
        
        return arr
    
# for [-1, 2, -3, 4, 5, 6] we get [-1, -3, 2, 4, 5, 6]

'''
Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct.

Example 1:

Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
'''





































