N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

boxes = [[] for i in range(N)]

print(boxes)

# それぞれの箱の中の荷物の大きさを表現
for i in range(N):
    a = A[i] - 1
    w = W[i]

    boxes[a].append(w)

# 荷物を軽い順に並べる(取り出しやすくするため)
for i in range(N):
    boxes[i].sort()

ans = 0

for i in range(N):
    box = boxes[i]

    # boxが2個以上だったら最後以外の要素を取り出して足すことでコストを出す
    if(len(box) >=2):
        # box[:-1]はboxの中で最後の要素を取り除いたもの
        ans += sum(box[:-1])

print(ans)
