def DFS(L, start, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt +=1
        return
    for i in range(start, n):
        DFS(L+1, i+1, sum + n_list[i])

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
m = int(input())
cnt = 0
DFS(0,0,0)
print(cnt)