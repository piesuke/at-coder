N = int(input())
strN = str(N)
amari1 = False
amari2 = False

amari_all = N % 3

for i in range(len(strN)):
    keta_num = int(strN[i])
    if keta_num % 3 == 1:
        amari1 = True
    if keta_num % 3 == 2:
        amari2 = True

if(amari_all == 0):
    print(0)

if(amari_all == 1):
    if(amari1 == True):
        if(len(strN) <= 1):
            print(-1)
        else:
            print(1)
    else:
        if(len(strN) <= 2):
            print(-1)
        else:
            print(2)
elif amari_all == 2:
    if amari2 == True:
         if(len(strN) <= 1):
            print(-1)
         else:
            print(1)
    else:
        if(len(strN) <= 2):
            print(-1)
        else:
            print(2)

