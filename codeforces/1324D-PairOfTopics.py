def countGoodPairs(n, a, b):
    diff = [a[i] - b[i] for i in range(n)]
    diff.sort()
    count = 0

    for i in range(n):
        if diff[i] > 0:
            count += n - i - 1
        else:
            l, r = i + 1, n - 1
            while l <= r:
                m = (l + r) // 2
                if diff[i] + diff[m] > 0:
                    r = m - 1
                else:
                    l = m + 1
            count += n - l

    return count

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(countGoodPairs(n, a, b))
