# N = int(input())

# tastes = [[0] * 2 for i in range(N)]


# for i in range(N):
#     tastes[i] = list(map(int, input().split()))
# max = 0

# maxList = [0,0]

# sameFList = [0,0]
# differentFList = [0,0]

# for i in range(N):
#     t = tastes[i]
#     if(maxList[1] < t[1]):
#         maxList = t

# for i in range(N):
#     t = tastes[i]
#     if(maxList[0] == t[0] and maxList[1] == t[1]):
#         continue
#     if(maxList[0] == t[0] and sameFList[1] < t[1]):
#         sameFList = t
#     if(maxList[0] != t[0] and differentFList[1] < t[1]):
#         differentFList = t

# same = maxList[1] + (sameFList[1] / 2)
# differ = maxList[1] + differentFList[1]

# sum = same if same > differ else differ
# print(int(sum))



N = int(input())

tastes = [[0] * 2 for i in range(N)]

for i in range(N):
    tastes[i] = list(map(int, input().split()))
max = 0

maxList = [0,0]
maxIndex = 0
for i in range(N):
    t = tastes[i]
    if(maxList[1] < t[1]):
        maxList = t
        maxIndex = i


for i in range(N):
    result = 0
    t = tastes[i]
    if(maxIndex == i):
        continue
    if(t[0] == maxList[0]):
        result = maxList[1] + (t[1] / 2)
    else:
        result = maxList[1] + t[1]
    if(max < result):
        max = result

print(int(max))
