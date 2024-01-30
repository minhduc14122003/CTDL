def reverse_list_in_place(index):
    left = 0
    right = len(index) - 1

    while left < right:
        index[left], index[right] = index[right], index[left]
        left += 1
        right -= 1
        
arr = [1, 2, 3, 4, 5, 6, 7]
reverse_list_in_place(arr)
print(arr)       



    