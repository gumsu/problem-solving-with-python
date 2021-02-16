# dy[i][j]는 그 칸까지 가는데 최소비용
# 0행과 0열은 누적하여 초기화
# 가운데 칸은 왼쪽칸vs윗칸 중 최소값을 택함
# d(2,2)에서 d(2,1)과 d(1,2)로 가지가 뻗음, 그 중 최소 비용 택함

def DFS(x, y):
    if dy[x][y] > 0: # 이미 값이 구해졌다면
        return dy[x][y]
    if x == 0 and y == 0 :
        return arr[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y]
        return dy[x][y]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)] # 메모이제이션
print(DFS(n-1, n-1))