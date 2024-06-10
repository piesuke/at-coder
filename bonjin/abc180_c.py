import math


N = int(input())

ans = set()
for i in range(1, N+1):
    if(math.sqrt(N) < i):
        break
    n = 0
    if(N % i == 0):
        ans.add(i)
        ans.add(N//i)

sortedSet = sorted(ans)
for i in range(len(list(sortedSet))):
    print(list(sortedSet)[i])