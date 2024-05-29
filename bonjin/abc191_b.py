N, X = map(int, input().split())
A = list(map(int, input().split()))

sum = []

for i in range(N):
    if(X != A[i]):
        sum.append(A[i])

print(*sum)