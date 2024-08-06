import itertools

N, K = map(int, input().split())
p = list(map(int, input().split()))


sumList = []
for i in range(N):
    sumList.append((p[i] + 1) / 2)

p_ex = []

p_ex_tmp = itertools.accumulate(sumList)

for i in p_ex_tmp:
    p_ex.append(i)

ans = 0

for i in range(N -K + 1):
   ans_tmp = 0
   if i == 0:
        ans_tmp = p_ex[i + K - 1]
   else:
       ans_tmp = p_ex[i + K - 1] - p_ex[i - 1]
   ans = max(ans, ans_tmp)

print(ans)