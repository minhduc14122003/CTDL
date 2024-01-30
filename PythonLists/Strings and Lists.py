a = 'spam'
b = list(a)
print(b)

#1
a = 'spam spam spam'
b = a.join(a)
print(b)

#2
a = 'spam-spam-spam'
delimiter = 'a'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))

