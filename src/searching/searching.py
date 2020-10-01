import random
import time

random = random.sample(range(20), 20) # range of 20 items including the numbers from 0 to 20
print(random)
searching_for = 15

def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
        
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #Your code here
    first = 0
    last = len(arr) - 1
    
    while first <= last:
        # Find the middle of the data.
        mid = (first + last) // 2
        
        if arr[mid] == target:
            return mid
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
        
    return -1 # not found

print("Linear Search =", linear_search(random, searching_for))
#print(binary_search([2, 4, 6, 4, 67, 988, 43, 56], [10]))
print("Binary Search =", binary_search(random, searching_for))