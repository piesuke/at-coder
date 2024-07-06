N = int(input())
S= str(input())
Q = int(input())

S = "0" + S
S = list(S)
flip = False

ans = ""
for i in range(Q):
    T, A, B = map(int, input().split())
    if(T == 1):
        if(flip == False):
            # 入れ替えができるコード
            S[A], S[B] = S[B], S[A]
        else:
            if(A <= N):
                A += N
            else:
                A -= N
            if(B <= N):
                B += N
            else:
                B -= N
            S[A], S[B] = S[B], S[A]
    if(T == 2):
        if(flip == True):
            flip = False
        else:
            flip = True

if(flip == True):
    remaining = S[1:]
    first = remaining[:N]
    second = remaining[N:]
    ans = second + first
else:
    remaining = S[1:]
    ans = remaining

print("".join(ans))