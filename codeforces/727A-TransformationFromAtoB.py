a, b = map(int, input().split())
seq = []

while b >= a:
    seq.append(b)

    if b == a:
        print("YES")
        print(len(seq))
        print(' '.join(map(str, seq[::-1])))
        exit()
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        print("NO")
        exit()
else:
    print("NO")

