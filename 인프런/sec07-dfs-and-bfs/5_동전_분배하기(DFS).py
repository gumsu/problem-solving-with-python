def DFS(L):
    global res
    if L == n:
        char = max(money) - min(money)
        if char < res:
            tmp = set() # 세 사람의 총액이 달라야함
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = char
        return
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]    


if __name__=="__main__":
    n = int(input())
    money = [0,0,0]
    coin = []
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)