array = [1, 2, 3, 4]

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i), str(j), sep = ',')
printPairs(array)            