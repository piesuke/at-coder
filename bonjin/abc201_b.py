N = int(input())

mountains = []

for i in range(N):
    S, T = map(str, input().split())
    I = int(T)
    mountains.append([I,S])

mountains.sort(reverse=True)

print(mountains[1][1])