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

# 4: Find the first element to occur k times in an array

L = [1,2,1,2,1,3,4,4,5,5]
k = 2

count = {}           # Start with an empty dictionary

for i in L:              # For every element in L
    if i in count:              # If the element is in the dictionary
        count[i] += 1              # Then increase its count by 1
    if i in count and count[i] == k:          # Check if the element is in count and its value is equal to k times
        print(i)
        break                # print element and break the loop
    else:
        count[i] = 1          # if the element is not in the dictionary, add it as a key and give it a value 1

#4. Find the nth (1st, 2nd, 3rd...) element to occur k times in an array
L = [1,2,1,2,1,3,4,4,5,5]
k = 2
n = 3
count = {}

for i in L:         # Storing number of times each element occurs 
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
    
found = 0         # Starting with the value 0, we stop at the value of found = n, and that value of i is the required element
for i in L:
    if count[i] == k:
        found += 1
        if found == n:
            print(i)
            break
            
# 5. Find duplicates in an array
L = [1,1,2,3,4,4,5,5]

count = {}

for i in L:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
for k, v in count.items():      # Iterating through key and values
    if v > 1:
        print(k)           # printing all the keys where the values are greater than 1


# 6. Rotate array to left d items
L = [1,2,3,4,5]
d = 2

one = L[:d]
two = L[d:]

output = two + one

print(output)

# 7. Find intersection of 2 sorted arrays

a = [1,2,3,4,5,8]
b = [3,6,7,8]

for i in a:
    if i in b:
        print(i)
