x = y = z = 0
  
n = int(input())
  
for _ in range(n):
  vx, vy, vz = map(int, input().split())
  x += vx
  y += vy
  z += vz
  
print("YES" if x == y == z == 0 else "NO")