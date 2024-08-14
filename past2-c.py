N = int(input())
S = []

for i in range(0, N):
    s1 = input()
    S.append(s1)

for i in reversed(range(0, N-1)):
    for j in range(1, (2*N -2)):
        if(S[i][j] == "#"):
            if(S[i+1][j-1] == "X" or S[i+1][j] == "X" or S[i+1][j+1] == "X"):
                list1 = list(S[i])
                list1[j] = "X"
                S[i] = ''.join(list1)

for i in S:
    print(i)
