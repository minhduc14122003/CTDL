def check_same_frequency(list1, list2):
    return sorted(list1) == sorted(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
result = check_same_frequency(list1, list2)

if result:
    print("True")
else:
    print("flase")