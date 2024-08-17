N, Q = map(int, input().split())

graph = []

for i in range(0,N):
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

for i in range(0, Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        query[1] -= 1
        query[2] -= 1
        graph[query[1]][query[2]] = True
    if query[0] == 2:
        followList = []

        index = 0
        query[1] -= 1
        for g in graph:
            if(g[query[1]]):
                followList.append(index)
            index += 1
        for i in followList:
            graph[query[1]][i] = True
    
    if query[0] == 3:
        to_follow = []
        query[1] -= 1
        
        for i in range(0, N):
            if(graph[query[1]][i]):
                for j in range(0, N):
                    if(graph[i][j] and j != query[1]):
                        to_follow.append(j)

        for w in to_follow:
            graph[query[1]][w] = True 


for i in range(0, N):

    for j in range(0, N):
        if(graph[i][j]):
            print("Y",end='')
        else:
            print("N",end='')
    print()