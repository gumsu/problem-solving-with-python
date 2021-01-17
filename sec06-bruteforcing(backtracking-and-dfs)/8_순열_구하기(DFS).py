def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    for i in range(1, n+1):
        if check[i] == 0:
            check[i] = 1
            res[L] = i
            DFS(L+1)
            check[i] = 0    # 호출하기전 행동했던 것을 취소해주는 작업
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*n
    check = [0]*(n+1)
    cnt = 0
    DFS(0)