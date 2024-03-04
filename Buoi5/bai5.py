my_dict = {'a': 5, 'b' : 4, 'c':2}

max_value_key = max(my_dict, key=my_dict.get)

print(max_value_key)
