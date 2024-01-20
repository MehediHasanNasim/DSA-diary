def binary_search(array, target):
    left, right = 0, len(array) - 1
    
    while left <= right:
        mid = left + (right - left) // 2 
        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1  

array = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
target = 5
result = binary_search(array, target)

# checking, is target found or not
if result != -1:
    print(f"Element {target} is found at index {result}")
else:
    print(f"Element {target} is not in the array")

    
    



