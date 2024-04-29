# reference https://qiita.com/wihan23/items/2b4402169469019be2e2
N = int(input())

# 1組、2組で分けて得点を格納する
c1 = [0]*N
c2 = [0]*N

for i in range(N):
  c, p = map(int, input().split())
  if c == 1:
    c1[i] = p
  else:
    c2[i] = p

# 各組で累積和 s1, s2を求める
s1 = [0]*(N+1)
s2 = [0]*(N+1)

for i in range(N):
  s1[i+1] = s1[i] + c1[i]
  s2[i+1] = s2[i] + c2[i]

# Q個のクエリに対し、L~R番までの合計を求める
# L番は和に含めるため、L-1番までの合計をマイナスする
Q = int(input())

for _ in range(Q):
  l, r = map(int, input().split())
  sum1 = s1[r] - s1[l-1]
  sum2 = s2[r] - s2[l-1]
  print(sum1, sum2)