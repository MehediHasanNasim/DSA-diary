myDict = {'nasim': 'he is a good boy',
          'tanvir': 'he is a bad boy'}
print(myDict['tanvir'])
# update / add element?
theDict = {'name': 'nasim',
           'age': 25}
theDict['age'] = 24
theDict['country'] = "bd"
print(theDict)

# Traversing dictionary?
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
traverseDict(theDict)

# searching dictionary?
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
        else: 'does not exist'
print(searchDict(theDict, 24))

# delete & all delete
myDict.pop('key')
myDict.clear()  # syntax: dictionary.clear()
del myDict('key')
print(myDict.get('age')) # syntax: dictionary.get(key, value)
print(sorted(myDict, reverse= True))
