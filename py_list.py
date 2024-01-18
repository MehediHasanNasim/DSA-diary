# Creating a list
fruits = ["apple", "banana", "orange", "grape"]

# Accessing elements
print(fruits[0])   # Output: "apple"
print(fruits[2])   # Output: "orange"

# Modifying elements
fruits[1] = "kiwi"
print(fruits)      # Output: ["apple", "kiwi", "orange", "grape"]

# Appending elements
fruits.append("mango")
print(fruits)      # Output: ["apple", "kiwi", "orange", "grape", "mango"]

# Removing elements
fruits.remove("orange")
print(fruits)      # Output: ["apple", "kiwi", "grape", "mango"]


# Iterating over a list
for fruit in fruits:
    print(fruit)
    
# Searching algorithm:
# searching for an element in the list
# in operator
myList = [10,20,30,40,50,60,70,80]
if 20 in myList:
    print(myList.index(20))
else:
    print("not exist")

# in linear search
def searchIndex(myList, value):
    for i in myList:
        if i == value:
            return myList.index(value)
    else:
        return "not exist"
print(searchIndex(myList, 50))
