n = int(input())
names_count = {}
  
for _ in range(n):
  name = input()
  
  if name in names_count:
    names_count[name] += 1
    print(f"{name}{names_count[name]}")
  else:
    names_count[name] = 0
    print("OK")