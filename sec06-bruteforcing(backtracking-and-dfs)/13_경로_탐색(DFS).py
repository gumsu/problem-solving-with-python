def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        print(*path)
    for i in range(1, n+1):
        if g[v][i] == 1 and check[i] == 0 :
            check[i] = 1
            path.append(i)
            DFS(i)
            path.pop()
            check[i] = 0

if __name__=="__main__":
    n, m = map(int, input().split())
    g= [[0]*(n+1) for _ in range(n+1)]
    check = [0]*(n+1)
    # 행렬 생성(방향 그래프)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = []
    path.append(1)
    # 1번 노드 체크하고 DFS(1) 호출
    check[1] = 1
    DFS(1)
    print(cnt)