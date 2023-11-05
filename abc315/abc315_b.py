M = int(input())

D = list(map(int, input().split()))

yearSum = 0

for i in D:
    yearSum += i
center = (yearSum + 1) /2
monthSum = 0

month = 0
day = 0

index = 0
for dayNum in D:
    month += 1
    thisMonthSum = monthSum + dayNum
    if(center <= thisMonthSum):
        day = center - monthSum
        break
    index += 1
    monthSum += dayNum

print(month,int(day))