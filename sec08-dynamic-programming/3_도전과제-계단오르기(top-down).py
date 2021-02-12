def DFS(stair):
    if dy[stair] > 0:
        return dy[stair]
    if stair == 1 or stair == 2:
        return stair
    else:
        dy[stair] = DFS(stair-1) + DFS(stair-2)
        return dy[stair]

if __name__=="__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))