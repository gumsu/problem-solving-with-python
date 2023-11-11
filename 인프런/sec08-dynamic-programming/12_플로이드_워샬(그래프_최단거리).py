# dis[i][j] i노드에서 j노드로 가는데 드는 최소 비용 값
n, m = map(int, input().split())
dis = [[5000]*(n+1) for _ in range(n+1)]

for i in range(n+1): #dis[i][i] = 0 초기화
    dis[i][i] = 0

for i in range(m):  # i -> j 바로 가는 것 초기화
    a, b, c = map(int, input().split())
    dis[a][b] = c

for k in range(1, n+1): # i -> k -> j 로 가는 것 갱신
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])


for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == 5000:
            print("M",end=' ')
        else:
            print(dis[i][j], end=' ')
    print()