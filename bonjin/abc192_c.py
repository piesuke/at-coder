N, K = map(int, input().split())

def g1(x):
    list = []
    for a in str(x):
        list.append(int(a))
    list.sort()
    num = 0
    for i, b in enumerate(list):
        num += b * (10**i)
    return num


def g2(x):
    list = []
    for a in str(x):
        list.append(int(a))
    list.sort(reverse=True)
    num = 0
    for i, b in enumerate(list):
        num += b * (10**i)
    return num

ans = 0
for c in range(K+1):
    if(c ==0):
        ans += N
    else:
        ans = g1(ans) - g2(ans)

print(ans)