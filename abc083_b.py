# https://atcoder.jp/contests/abc083/tasks/abc083_b

N, A, B = map(int, input().split())

sum = 0

for i in range(1, N+1):
    sum_digit = 0
    x = [int(a) for a in str(i)]
    for j in x:
        sum_digit += j
    if(sum_digit >= A and sum_digit <=B):
        sum += i

print(sum)