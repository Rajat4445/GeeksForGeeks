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
