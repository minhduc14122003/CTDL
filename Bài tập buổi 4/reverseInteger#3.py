def reverse_integer(a):
    reversed_a = 0
    while a > 0:
        remainder = a % 10
        reversed_a = reversed_a * 10 + remainder
        a = a // 10
    return reversed_a

integer = 12
print(reverse_integer(integer))
