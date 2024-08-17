# 隣接行列を使った解法

# N, M, Q = map(int, input().split())

# graph = []

# # グラフを作成する
# for i in range(0, N):
#     row = []
#     for j in range(0,N):
#         row.append(False)
    
#     graph.append(row)

# # 辺があるものをTrueにする
# for i in range(0, M):
#     u, v = map(int, input().split())

#     # 頂点番号は全て-1する
#     u -= 1
#     v -= 1

#     # 互いに辺で結ばれている
#     graph[u][v] = True
#     graph[v][u] = True

# # 頂点の色のリスト
# C = list(map(int, input().split()))

# for i in range(0, Q):
#     query = list(map(int, input().split()))

#     # スプリンクラーを起動するクエリ
#     if query[0] == 1:
#         x = query[1]

#         x -= 1

#         print(C[x])

#         for i in range(0, N):
#             # 頂点xと頂点iの間に辺があるとき
#             if graph[x][i]:
#                 C[i] = C[x]

#     # スプリンクラーを起動しないクエリ
#     if query[0] == 2:
#         x = query[1]
#         y = query[2]

#         x -= 1

#         print(C[x])

#         # 頂点xの色をyに書き換える
#         C[x] = y



# 隣接リストを使った解法


N, M, Q = map(int, input().split())

graph = []

# グラフを作成する
for i in range(N):
    graph.append([])

for i in range(M):
    u, v = map(int, input().split())

    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# 頂点の色のリスト
C = list(map(int, input().split()))

num = 0
for i in range(0, Q):
    num += 1
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])

        for i in graph[x]:
            C[i] = C[x]
    if query[0] == 2:
        x = query[1]
        y = query[2]
        x -= 1
        print(C[x])
        C[x] = y