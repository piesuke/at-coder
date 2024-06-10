def includeSevenBaseNumberTen(n):
    if('7' in str(i)):
        return True
    return False

def includeSevenBaseNumberEight(x):
    s = ''
    while x > 0:
        s=str(x%8)+s
        x = x//8
    if '7' in s:
        return True
    return False

N = int(input())
ans = 0
for i in range(1, N+1):
    if includeSevenBaseNumberTen(i) == False  and includeSevenBaseNumberEight(i) == False:
        ans +=1
print(ans)
