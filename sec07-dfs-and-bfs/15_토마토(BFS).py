from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
check = [[0]*n for _ in range(m)]
Q = deque()
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            Q.append((i, j))

while Q:
     tmp = Q.popleft()

     for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]
        if 0 <= xx < m and 0 <= yy < n and box[xx][yy] == 0:
            box[xx][yy] = 1
            check[xx][yy] = check[tmp[0]][tmp[1]]+1
            Q.append((xx, yy))

flag = 1
for i in range(m):
    for j in range(n):
        if box[i][j] == 0:
            Q.append((i, j))
            flag = 0

result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if check[i][j] > result:
                result = check[i][j]
    print(result)
else:
    print(-1)