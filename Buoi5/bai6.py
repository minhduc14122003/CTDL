def reverse_dict(input_dict):
    reversed_dict = {value: key for key, value in input_dict.items()}
    return reversed_dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
result_dict = reverse_dict(my_dict)
print(result_dict)