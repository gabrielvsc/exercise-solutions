n, m, a, b = map(int, input().split())

firstOption = n * a
secondOption = b * (n // m) + a * (n % m)
thirdOption = b * ((n + m - 1) // m)

print(min(firstOption, secondOption, thirdOption))