n = int(input())

# dy[2]는 제일 꼭대기에 2번 벽돌을 놓는다고 가정할 때 최대 높이
# dy[4]는 제일 꼭대기에 4번 벽돌을 놓는다고 가정할 때 최대 높이
bricks = []
for _ in range(n):
    area, height, weight = map(int, input().split())
    bricks.append((area, height, weight))

bricks.sort(reverse=True) # 밑면 넓이를 기준으로 내림차순
dy = [0]*n
dy[0] = bricks[0][1] # 첫번째 벽돌의 높이를 넣어줌

for i in range(1, n):
    maxHeight = 0
    for j in range(i-1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > maxHeight:
            maxHeight = dy[j]
    
    dy[i] = maxHeight + bricks[i][1]

print(max(dy))
