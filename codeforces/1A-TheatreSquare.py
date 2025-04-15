import math
    
n = input().split()
    
fn = math.ceil(int(n[0]) / int(n[2]))
fm = math.ceil(int(n[1]) / int(n[2]))
    
print(fn * fm)