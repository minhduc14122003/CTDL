def powerOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powerOf2(int(n/2))
        curr = prev*2
        print(curr)
        return curr
print(powerOf2(50))    
