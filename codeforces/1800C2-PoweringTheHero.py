import heapq

t = int(input())
testCases = []

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    testCases.append((n, cards))

for i in range(t):
    n, cards = testCases[i]
    bonusHeap = []
    totalPower = 0

    for power in cards:
        if power > 0:
            heapq.heappush(bonusHeap, -power)
        elif power == 0:
            if bonusHeap:
                totalPower -= heapq.heappop(bonusHeap)

    print(totalPower)
