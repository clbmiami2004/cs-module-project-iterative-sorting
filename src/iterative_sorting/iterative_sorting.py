import time
# TO-DO: Complete the selection_sort() function below
start = time.time()
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

random_list_of_numbers = [1, 10, 7, 8, 2, 23, 6]
selection_sort(random_list_of_numbers)
end = time.time()
print(f"This is my runtime {end - start} seconds")
print(random_list_of_numbers)

# TO-DO:  implement the Bubble Sort function below
start1 = time.time()
def bubble_sort(arr):
    # We set swapped to true so the loop runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                # Swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Set the flag to true so we'll loop again
                swapped = True
    
    return arr

# Verify it works:
random_list_of_numbers1 = [4, 7, 2, 30, 12, 10, 9, 22]
bubble_sort(random_list_of_numbers1)
end1 = time.time() - start1
finalTime = f"{end1: .21f}"
print(finalTime)
#print("My processing time for bubble sort is =", end1)
print(random_list_of_numbers1)


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
