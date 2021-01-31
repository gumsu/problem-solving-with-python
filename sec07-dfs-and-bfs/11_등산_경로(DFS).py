def DFS(x, y):
    global cnt
    if x == ex and y == ey :
        cnt += 1
    else:
        for z in range(4):
            xx = x + dx[z]
            yy = y + dy[z]
            if 0<= xx < n and 0<= yy < n and mountain[xx][yy] > mountain[x][y]:
                DFS(xx, yy)

if __name__ == "__main__":
    n = int(input())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    max = -2147000000
    min = 2147000000

    for i in range(n):
        tmp = mountain[i]
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
    DFS(sx, sy)
    print(cnt)