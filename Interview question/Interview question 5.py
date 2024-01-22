arrayA = [1, 2, 3, 4]
arrayB = [5, 6, 7, 8]
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))
printUnorderedPairs(arrayA, arrayB)              