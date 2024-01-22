array = [1, 2, 3, 4, 5, 6]

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i], array[j], sep = ',')
printUnorderedPairs(array)           
