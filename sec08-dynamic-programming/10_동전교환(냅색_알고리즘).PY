n = int(input())
coins = list(map(int, input().split()))
m = int(input())
#dy[j] j원을 거슬러주는데 사용된 동전의 최소 개수
dy = [m]*(m+1)
dy[0] = 0

# while coins:
#     coin = coins.pop(0)
#     for i in range(coin, m+1):
#         dy[i] = min(dy[i], dy[i-coin]+1)

for i in range(n):
    for j in range(coins[i], m+1):
        dy[j] = min(dy[j], dy[j-coins[i]] + 1)

print(dy[m])