def canDivideEvenly(w):
    if w % 2 == 0 and w >= 4:
        return 'YES'
    else:
        return 'NO'
    
w = int(input())
print(canDivideEvenly(w))