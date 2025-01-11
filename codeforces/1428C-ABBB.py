t = int(input())
testCases = [input().strip() for _ in range(t)]
out = []

for test in testCases:
    stack = []
    for char in test:
        stack.append(char)
        
        
        if len(stack) >= 2 and (stack[-2] + stack[-1] in ("AB", "BB")):
            stack.pop()
            stack.pop()
    print(len(stack))
