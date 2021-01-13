def DFS(L, sum, tsum):
    global result
    if sum + (total-tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum

    else:
        DFS(L+1, sum+dogs[L], tsum+dogs[L])
        DFS(L+1, sum, tsum+dogs[L])

if __name__=="__main__":
    c, n = map(int, input().split())
    dogs = [int(input()) for _ in range(n)]
    total = sum(dogs)
    result = -2147000000
    DFS(0, 0, 0)
    print(result)