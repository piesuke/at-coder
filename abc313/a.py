# https://atcoder.jp/contests/abc313/tasks/abc313_a

N = int(input())
p = list(map(int, input().split()))

target = p[0]

necessary = 0

for index, i in enumerate(p):
    if i == 0:
        continue
    if i > target:
        if necessary < i - target:
            necessary = i - target + 1
    if index != 0 and necessary == 0 and i == target:
        necessary = 1

print(necessary)