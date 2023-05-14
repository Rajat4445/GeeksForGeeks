# Pasting all the solution by me for the questions

# 1. Find the kth largest/smallest item from a list

L = [12,23,1,4,56,34,22,3]
k=3

def minimum(arr):              ## Function outputs the minimum element in the array
    mini = arr[0]
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
            
    return mini

sorted_array = []        # We will store the sorted array (ascending) here

while len(L)!=0:                         # Appends the smallest element in L to sorted array and then removes that element from L
    sorted_array.append(minimum(L))
    L.remove(minimum(L))
    
print(sorted_array)
print(f"{k}th largest = {sorted_array[-k]}")
print(f"{k}th smallest = {sorted_array[k-1]}")



# # 2. Check if an array is sorted
L = [1,2,3,4,5]

def check_sorted(arr):       # The function checks if (i+1)th element is greater than the ith element, returns True else False
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            return False
    return True
    
print(check_sorted(L))

# 3. Find Min/Max in a given array
arr = [21,1,0,34,23,54,11,10, 102]

mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
    if arr[i]<mini:
        mini = arr[i]
    elif arr[i]>maxi:        ## elif is used when we want to check multiple conditions in the same loop 
        maxi = arr[i]
        
print(mini, maxi)






