def DFS(L, sum):
    global res
    if L == n+1 :
        if sum > res:
            res = sum
        return
    else:
        if L+t[L] <= n+1:
            DFS(L+t[L], sum+p[L])   # 상담 O
        DFS(L+1, sum)   # 상담 X

if __name__=="__main__":
    n = int(input())
    t = [0]
    p = [0]
    for _ in range(n):
        day, money = map(int,input().split())
        t.append(day)
        p.append(money)
    res = -2147000000
    DFS(1, 0)
    print(res)