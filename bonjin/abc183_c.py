# 全探索を使う
# 順列はitertools.permutationsで出すことができる
import itertools

N, K = map(int, input().split())

# 0 1 10 100 みたいなやつ 個数はN
# 都市iから都市jまでの距離を表している
time = []
for i in range(N):
    T = list(map(int, input().split()))
    time.append(T)

ans = 0

# itertools.permutationsでrange(1, N)の順列が取れる
# [1,3,2]とか [4,2,1]とか
for root in itertools.permutations(range(1, N)):
    now_time = 0
    # 都市1始まりなのでインデックスは0
    now_time+=time[0][root[0]]
    now_city=root[0]

    for i in range(1, N-1):
        to_city = root[i]
        now_time+=time[now_city][to_city]
        now_city=to_city

    now_time+=time[now_city][0]
    if now_time ==K:
        ans+=1

print(ans)