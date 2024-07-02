N = int(input())

array = list(map(int, input().split()))
ans = 0

for i in range(2* N - 2):
  if(array[i] != array[i + 1] and array[i] == array[i + 2] ):
    ans += 1

print(ans)
