def fibo(position):
    if position == 1:
        return 1
    if position <= 0:
        return 0
    else:
        f = fibo(position=position-1) + fibo(position=position-2) 
        return f
# 1 1 2 3 5 8 13, 21, 34, 55
print(fibo(40))