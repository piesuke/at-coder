# 少数を出来るだけ扱わないようにする。計算が微妙にミスる場合があるので
N ,X = map(int, input().split())

cups = 0
sum = 0
isFinish = False
for i in range(N):
    V, P = map(int, input().split())
    alcohol = V * P
    cups+= 1
    if(sum +alcohol > X * 100 ):
        print(cups)
        isFinish = True
        break
    else:
        sum += alcohol

if(isFinish == False):
    print(-1)