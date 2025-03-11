# Definition: 
'''Selection Sort is a simple sorting algorithm that repeatedly finds the smallest (or largest) element from the unsorted part and moves it to the correct position.'''

# How it Works: 
'''
1. Start with the first element and assume it's the smallest.
2. Compare it with all other elements in the list.
3. If a smaller element is found, update the smallest value.
4. Swap the smallest element with the first element.
5. Move to the next position and repeat the process for the remaining list.
6. Continue until the entire list is sorted.
'''

# Pseudocode 
'''
function selectionSort(arr):
    for i from 0 to length(arr) - 1:
        min_index = i
        for j from i+1 to length(arr):
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr[i], arr[min_index])
    return arr 
'''

# Python
def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

mylist = [3, 5, 2, 6, 8, 2, 9]
print(selectionSort(mylist))


# Python (optimized version)
def selectionSortOptimized(arr):
    for i in range(len(arr)):
        min_index = i
        swapped = False  # Track if a swap happens
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                swapped = True
        if swapped:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

mylist = [3, 5, 2, 6, 8, 2, 9]
print(selectionSortOptimized(mylist))
