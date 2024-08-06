A = []

M = []

for _ in range(0,3):
    row = list(map(int, input().split()))
    A.append(row)

for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(False)
    M.append(row)


N = int(input())

for _ in range(0, N):
    B = int(input())
    for a in range(0, 3):
        for el in range(0, 3):
            if(A[a][el] == B):
                M[a][el] = True

bingo = False


# 横
for i in range(0, 3):
    if(M[i][0] and M[i][1] and M[i][2]):
        bingo = True
        break
# 縦
for i in range(0, 3):
    if(M[0][i] and M[1][i] and M[2][i]):
        bingo = True
        break

# 斜め
if(M[0][0] and M[1][1] and M[2][2]):
    bingo = True

if(M[0][2] and M[1][1] and M[2][0]):
    bingo = True

if bingo:
    print("Yes")
else:
    print("No")