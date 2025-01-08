n, q = map(int, input().split())
a = list(map(int, input().split()))

countOnes = sum(a)

def attr(x):
    global countOnes
    if a[x] == 1:
        countOnes -= 1
    else:
        countOnes += 1
    a[x] = 1 - a[x]

def findKthLargest(k):
    return 1 if k <= countOnes else 0

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        attr(x - 1)
    elif t == 2:
        print(findKthLargest(x))