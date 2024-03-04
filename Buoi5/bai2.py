def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result_dict = merge_dicts(dict1, dict2)
print(result_dict)
