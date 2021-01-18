def DFS(L, start):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        cnt += 1
        print()
        return
    for i in range(start, n+1):
        res[L] = i
        DFS(L+1, i+1)

n, m = map(int, input().split())
res = [0]*(n+1)
cnt = 0
DFS(0, 1)
print(cnt)