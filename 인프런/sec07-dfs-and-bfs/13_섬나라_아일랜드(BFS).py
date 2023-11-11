from collections import deque

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

Q = deque()

dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, 1, 1, -1, -1]

for i in range(n):
    for j in range(n):
        if island[i][j] == 1:
            island[i][j] = 0
            Q.append((i,j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and island[x][y] == 1:
                        island[x][y] = 0
                        Q.append((x,y))
            cnt += 1
print(cnt)