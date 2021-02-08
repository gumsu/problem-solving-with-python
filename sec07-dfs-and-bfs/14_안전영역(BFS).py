import sys
sys.setrecursionlimit(10**6)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def DFS(x, y, h):
    check[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and check[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)

if __name__=="__main__":

    n = int(input())
    cnt = 0 # 안전 영역이 몇 개 인가?
    res = 0 # 최대 개수
    board = [list(map(int, input().split())) for _ in range(n)]
    
    # 높이가 바뀔 때마다 새로 체크배열 생성
    for h in range(100):
        check = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if check[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
    
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)
                