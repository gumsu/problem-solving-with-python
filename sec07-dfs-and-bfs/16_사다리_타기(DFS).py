def DFS(x, y):
    if x == 0:
        print(y)
        return
    if 0 <= y-1 and board[x][y-1] == 1:
        board[x][y-1] = 2
        DFS(x, y-1)
    elif y+1 < 10 and board[x][y+1] == 1:
        board[x][y+1] = 2
        DFS(x, y+1)
    elif 0<= x-1 and board[x-1][y] == 1:
        board[x-1][y] = 2
        DFS(x-1, y)
    
board = [list(map(int,input().split())) for _ in range(10)]

for i in range(10):
    if board[9][i] == 2:
        start = i
        break

DFS(9, start)