import math

def main():
    A, B, C = map(int, input().split())  # 整数の入力
    S = math.gcd(math.gcd(A, B), C)      # A, B, Cの最大公約数を計算
    result = (A // S - 1) + (B // S - 1) + (C // S - 1)  # 商から1を引いたものの合計
    print(result)  # 結果の出力

if __name__ == "__main__":
    main()