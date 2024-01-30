myLists = [1, 2, 3, 4, 5, 6, 7]
print(myLists)
myLists.insert(1, 33)
print(myLists)

#1
myLists.append(100)
print(myLists)

#2
newLists = ['H', 'E', 'L', 'L', 'O']
myLists.extend(newLists)
print(myLists)

#3
myLists = ['H', 'E', 'L', 'L', 'O']
print(myLists[1:4])

#4
print(myLists[2:])

#5
print(myLists[:2])

#6
myLists[0:2] = ['x', 'y']
print(myLists[:])

#7
myLists = ['H', 'E', 'L', 'L', 'O']
myLists.pop(2)
del myLists[1:3]
myLists.remove('H')
print(myLists)