N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

oneSum = 0
twoSum = 0

for i,a in enumerate(S):
    score = a[1]
    if a[0] == 1:
        oneSum = oneSum + score
    if a[0] == 2:
        twoSum = twoSum + score

Q = int(input())

for _ in range(Q):
    l, r = map(int, input().split())
