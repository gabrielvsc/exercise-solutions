t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
 
    if n == 1:
        print(1)
        continue
 
    tb = (n * (n - 1)) // 2
    z = k // (n - 1)
 
    if k >= tb:
        print(1)
    elif k >= (n - 1):
        print(1)
    elif z == n:
        print(z)
    else:
        print(n - z)