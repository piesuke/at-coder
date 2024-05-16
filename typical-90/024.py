# A==Bにするための必要な回数を求める
## K-必要な回数が偶数だったら何があっても同じになるので良い
def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline

    N, K = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))

    # Ⅰ. 最低限必要な操作回数（ 各項の差異 | Bi - Ai | の合計 ）を求める
    need = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            continue
        else:
            distance = abs(B[i] - A[i])
            need += distance
            
    #  Ⅱ. 操作回数がK回を超えないか判定
    #  Ⅲ. 残りの回数が偶数であるか判定 K-操作回数が偶数だったら、あとは何をやっても数を戻せるため
    print('Yes' if need <= K and (K - need) % 2 == 0 else 'No')


if __name__ == '__main__':
    main()