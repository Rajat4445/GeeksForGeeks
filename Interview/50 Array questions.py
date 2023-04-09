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
  
class Solution:
    def sortArr(self, arr, n):      
                    
        return sorted(arr)                 ## Built-in function in python
    
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
    count = 0
    
    for i in range(n):
        if arr[i] == x:
            count += 1
        else:
            count += 0
            
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

    # Update the array with the sorted values
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
        n_arr = [i for i in arr if i<0]
        p_arr = [i for i in arr if i>=0]
        
        return p_arr + n_arr
        

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
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        out = a+b
        
        return len(set(out))

'''
Given an array, rotate the array by one position in clock-wise direction.
Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
'''
def rotate( arr, n):
    
    last = []
    first = []
    
    for i in range(n):
        if i<n-1:
            last.append(arr[i])
        else:
            first.append(arr[i])
            
    output = first+last
    
    return output

'''
brr = arr.copy()
    
arr[0] = brr[-1]
arr[1:n] = brr[0:n-1]
'''

'''
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
'''
class Solution:
    def MissingNumber(self,array,n):
        array_set = set(array)   # The reason for not using the array has been mentioned below
        
        for i in range(1, n+1):
            if i not in array_set:
                return i
# However, the advantage of using a set is that the in operator performs a search in constant time O(1), 
# whereas searching in a list using the in operator would have a time complexity of O(n).


'''
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.
'''

class Solution:    # Try to understand this with arr = [1,2,3,4,5] and K = 6
    def getPairsCount(self, arr, n, k):                  ##(Hash Table Approach) , it is optimised
        # create a hash table to store the count of each number in arr
        count = {}
        for x in arr:                           ## Inserts how many time each element occurs as a key, value pair
            count[x] = count.get(x, 0) + 1          # Get is a dictionary method, .get(x,0), if x is available get its value, else get value as 0

        # iterate over the array and check for pairs
        answer = 0
        for x in arr:
            if k-x in count:
                answer += count[k-x]
            if k-x == x:  # if k-x is equal to x, then we need to subtract 1 from count[k-x], we do this as x paired with iteself (X,X) would give k
                answer -= 1

        # divide the answer by 2 since each pair is counted twice
        return answer // 2

##(My Approach)

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        output = [[i,j] for i in range(n) for j in range(n) if arr[i]+arr[j]==k]

        out_1 = output.copy()  

        for i in out_1:
            if i[::-1] in output:
                output.remove(i)
                
        answer = len(output)
                
        return answer


'''
Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

Note: The extra space is only for the array to be returned.
Try and perform all operations within the provided array. 

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: N=4 and all elements from 0
to (N-1 = 3) are present in the given
array. Therefore output is -1.
'''
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	count = {}
    	for i in arr:
    	    count[i] = count.get(i, 0) + 1
    	    
    	out = []	    
    	for k, v in count.items():
    	    if v>1:
    	        out.append(k)
    	        
    	if len(out)==0:
    	    out.append(-1)

    	return out
    
    
class Solution:                       ## Optimsed solution with O(n)
    def duplicates(self, arr, n): 
    	# code here
    	count = {}
    	
    	for i in arr:
    	    count[i] = count.get(i,0) + 1
    	    
    	duplicates = [x for x,v in count.items() if v>1]
    	
    	return sorted(duplicates) or [-1]
    	    
'''
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
'''
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        set_a = set(A)
        set_b = set(B)
        set_c = set(C)
        
        out_1 = set_a.intersection(set_b)
        out = set_c.intersection(out_1)
        
        return sorted(list(out))


'''
Given an array arr[] of size n, find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

Note:- The position you return should be according to 1-based indexing. 

Example 1:

Input:
n = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation: 
5 is appearing twice and 
its first appearence is at index 2 
which is less than 3 whose first 
occuring index is 3.
'''

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        
        d = {}
        min_index = n+1
        
        for i in range(n):
            if arr[i] in d:
                if freq[arr[i]] < min_index: # changes value of index as first occurence of repeated element
                    min_index = freq[arr[i]]
      
            else:
                freq[arr[i]] = i+1      # Stores first 1-based index value of element (minimum)
                
        if min_index == n+1:
            return -1
        
        return min_index


'''
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.

Example 1:

Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is 
the only number occuring once.
Hence, the output is 3. 
'''
class Solution:
    def firstNonRepeating(self, arr, n):      # Not time optimsed, since we are iterating thorugh each element
        # Complete the function
        count = [i for i in arr if arr.count(i) ==1]
        
        return count[0] or 0
    
    
class Solution:
    def firstNonRepeating(self, arr, n):       # Optimsed approach
        # Complete the function
        count = {}
        
        for i in range(n):
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1
                
        out = [i for i in arr if count[i]==1]
        
        return out[0] or 0


 '''
 Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

Example 1:

Input:
n = 7
A[] = {1,0,0,1,0,1,1}
Output: 8
Explanation: The index range for the 8 
sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), 
(4, 5) ,(2, 5), (0, 5), (1, 6)
'''
    
class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):       # Solution works but has O(n^3) time complexity
        #Your code here
        out = []
        
        for i in range(0,n):
            for j in range(1, n):
                if j>i and arr[i:j+1].count(0)==arr[i:j+1].count(1):
                    out.append((i,j))
                    
        return len(out)
            

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self, arr, n):     # (optimised approach, using hash table)
        count = 0
        diff_map = {0: 1} # initialize with 0 as key and 1 as value
        diff = 0
        
        for i in range(n):
            if arr[i] == 1:
                diff += 1
            else:
                diff -= 1
            
            if diff in diff_map:
                count += diff_map[diff]
                diff_map[diff] += 1
            else:
                diff_map[diff] = 1
                
        return count

'''
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number.

Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Explanation : Positive elements : 9,4,5,0,2
Negative elements : -2,-1,-5,-3
As we need to maintain the relative order of
postive elements and negative elements we will pick
each element from the positive and negative and will
store them. If any of the positive and negative numbers
are completed. we will continue with the remaining signed
elements.The output is 9,-2,4,-1,5,-5,0,-3,2.
'''



