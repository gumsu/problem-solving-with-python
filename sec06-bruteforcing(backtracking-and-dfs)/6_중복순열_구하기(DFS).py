def DFS(L):
    global cnt
    # 종료 조건
    if L == m:
        print(*res)
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)