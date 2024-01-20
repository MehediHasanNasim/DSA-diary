def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not in the array

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
    
# OR

def LinearSearch(array, targetVal):
    for i in range(len(array)):
        if array[i] == targetVal:
            return i 
    return -1 

print(LinearSearch([23,4,45,44,34,5], 44))
    
    
    
    
    
    
    
    
    