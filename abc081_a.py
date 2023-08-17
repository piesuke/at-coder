# https://atcoder.jp/contests/abc081/tasks/abc081_a
math = input()

# 数字を3桁に分解
a = int(math[0])
b = int(math[1])
c = int(math[2])

list = [a,b,c]

result = 0

for i in list:
    if i == 1:
        result = result + i

print(result)