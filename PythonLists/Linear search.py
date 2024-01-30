myList = [10, 20, 30, 40]
def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1
print(linear_search(myList, target = 50))  

#1
for index, value in enumerate(myList, 2):
    print(index, value)
