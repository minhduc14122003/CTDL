arr = [1, 2, 3, 4, 4, 5, 6, 6]
element = 4

def numberofOccurences(arr, element):
    occurences = arr.count(element)
    return occurences
print("So lan xuat hien cua phan tu:", element , "trong mang la:", numberofOccurences(arr, element))

           