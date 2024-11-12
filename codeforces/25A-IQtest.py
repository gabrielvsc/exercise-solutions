n = int(input())
array = list(map(int, input().split()))
  
indexDiff = 0
lastMod = None
  
for i in range(n):
  if lastMod == None:
    lastMod = array[i] % 2
  else:
    if lastMod != array[i] % 2:
      if i == 1 and array[i] % 2 == array[i + 1] % 2:
        indexDiff = 0
        break
      else:
        indexDiff = i
        break
            
print(indexDiff + 1)