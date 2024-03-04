def concatenate_strings(input_tuple):
    # Nối các chuỗi trong tuple bằng khoảng trắng
    return ' '.join(input_tuple)
input_tuple = ('hello','world','from','Python')
output_string = concatenate_strings(input_tuple)
print(output_string)