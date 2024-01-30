prev_list = [1, 2, 3]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)

#1
laguage = 'Python'
new_list = [letter for letter in laguage]
print(new_list)

#2
prev_list = [-1, -10, -20, -30, 2, -90, 60, 45, 20]
new_list = [number for number in prev_list if number > 0]
print(new_list)

#3
prev_list = [-1, -10, -8, 8, 11, 30, -4, 40, 50]
new_list = [number if number > 0 else 0 for number in prev_list]
print(new_list)

#4
def get_number(number):
    if number > 0:
        return number
    else:
        return 'negative number'
    
prev_list = [-1, -10, -20, -30, 2, -90, 60, 45, 20]
new_list = [get_number(number) for number in prev_list]
print(new_list)   




