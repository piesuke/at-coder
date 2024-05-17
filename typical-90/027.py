n = int(input())
set_ = set()

for i in range(1, n+1):
  s = input()
  if s in set_:
    continue
  set_.add(s)
  print(i)