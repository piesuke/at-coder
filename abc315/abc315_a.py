S = input()
list = list(S)
target = ["a", "e", "i", "o", "u" ]
sum = ""
for a in list:
    if(a in target):
        continue
    else:
        sum += a

print(sum)