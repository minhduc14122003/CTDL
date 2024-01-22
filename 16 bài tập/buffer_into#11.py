import array

arr = array.array('i', [1, 2, 3, 4])
buffer_information = arr.buffer_info()
print(buffer_information)