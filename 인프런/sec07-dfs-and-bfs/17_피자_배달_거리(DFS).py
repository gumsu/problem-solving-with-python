def DFS(L, s):
    global res
    if L == m:
        sum = 0 # 도시의 피자 거리
        for j in range(len(house)):
            x1 = house[j][0]
            y1 = house[j][1]

            dis = 2147000000

            for x in combination:
                x2 = pizza[x][0]
                y2 = pizza[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pizza)):
            combination[L] = i
            DFS(L+1, i+1)
if __name__=="__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    house = []
    pizza = []
    combination = [0]*m # 피자집을 6개 중 4개를 선택 6C4
    res = 2147000000

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                house.append((i,j))
            elif board[i][j] == 2:
                pizza.append((i,j))
    
    DFS(0,0)
    print(res)