newTuple = ('a', 'b', 'c', 'd')
newTuple1 = tuple('abcd')
print(newTuple1)
print(newTuple)

# search tuple?
def searchTuple(ptuple, element):
    for i in ptuple:
        if i == element:
            return newTuple.index(i)
    return "does not exist"

print(searchTuple(newTuple, 'c'))
# convert list to tuple?
print(tuple([1,2,3,4]))

