def DFS(x, y):
    global cnt
    cnt += 1
    city[x][y] = 0

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and city[xx][yy] == 1:
            DFS(xx, yy)

if __name__ == "__main__":
    n = int(input())
    city = [list(map(int, input())) for _ in range(n)]

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    res = []

    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    
    print(len(res))
    res.sort()
    for z in res:
        print(z)