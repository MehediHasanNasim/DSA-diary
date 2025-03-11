# Definition: 
'''Bubble Sort is a simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order. It keeps passing through the list until it is completely sorted.'''

# How it Works: 
'''
1. Start from the first element and compare it with the next one. 
2. If the first element is greater than the second, swap them. 
3. Move to the next pair and repeat the process for the whole list. 
4. After one complete pass, the largest element moves to the last position. 
5. Repeat the process for the remaining elements until the list is fully sorted.'''

# Pseudocode 
'''
function bubbleSort(arr):
    n = length of arr
    for i from 0 to n-1:
        for j from 0 to n-1-i:
            if arr[j] > arr[j+1]:  # Swap if needed
                swap(arr[j], arr[j+1])
    return arr 
'''

# Python
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    return customList

mylist = [3,5,2,6,8,2,9]
print(bubbleSort(mylist))


# Python (optimized version)
def bubbleSortOptimized(customList):
    n = len(customList)
    for i in range(n - 1):
        swapped = False  # Track if a swap happens
        for j in range(n - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
                swapped = True
        if not swapped:
            break  # Stop if no swaps happened
    return customList
