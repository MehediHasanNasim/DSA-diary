# Bubble Sort
# def bubbleSort(customList):
#     for i in range(len(customList)-1):
#         for j in range(len(customList)-i-1):
#             if customList[j] > customList[j + 1]:
#                 customList[j], customList[j + 1] =  customList[j + 1], customList[j]
                
#     print(customList)
    
# cList = [2,1,3,5,7,4,9,0]
# bubbleSort(cList)

# Insertion Sort
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j+1] = key 
    print(customList)
cList = [2,1,3,5,7,4,9,0]
insertionSort(cList)