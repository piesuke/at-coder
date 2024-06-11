#  愚直にやるだけ系問題について、解き方を工夫することでTLEを防ぐ
N, K = map(int, input().split())

friends = []
for i in range(N):
    A,B = map(int, input().split())
    friends.append([A,B])

village_num = 0

village_num += K

friends.sort()

for i in range(N):     
    friend_village=friends[i][0]     
    friend_money=friends[i][1]
    if friend_village<=village_num:         
        village_num+=friend_money     
    else:         
        break

print(village_num)



