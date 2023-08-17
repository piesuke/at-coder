# https://atcoder.jp/contests/abc086/tasks/abc086_a

a,b = list(map(int, input().split()))

product = a * b

if product % 2 == 0:
    print('Even')
else:
    print('Odd')