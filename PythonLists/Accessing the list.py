shoppingList = ['milk', 'butter', 'cheese', 'cream']
print(shoppingList)

#1
shoppingList = ['milk', 'butter', 'cheese', 'cream']
print(shoppingList[2])

#2
print('milk' in shoppingList)

#3
print(shoppingList[-3])

#4
for i in shoppingList:
    print(i)

#5
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + ' +1'
    print(shoppingList[i])

        