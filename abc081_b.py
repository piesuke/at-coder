# https://atcoder.jp/contests/abc081/tasks/abc081_b

def how_many_times_divisible(n):
	ans = 0
	while n % 2 == 0:
		n /= 2
		ans += 1
	return ans
 
n = int(input())
a = map(int, input().split())
# minを使っているのは、一番最初に割り切れない数を探したら良いため。
ans = min(map(how_many_times_divisible, a))
 
print(ans)

