x = 0
n = int(input())
for _ in range(n):
    op = input()
    
    if op == "++X" or op == "X++":
        x = x + 1
    else:
        x = x - 1
print(x)