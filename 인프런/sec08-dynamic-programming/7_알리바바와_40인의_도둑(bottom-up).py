# dy[i][j]는 그 칸까지 가는데 최소비용
# 0행과 0열은 누적하여 초기화
# 가운데 칸은 왼쪽칸vs윗칸 중 최소값을 택함

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = arr[0][0]
for i in range(1, n):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[0][i-1] + arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]

print(dy[n-1][n-1])