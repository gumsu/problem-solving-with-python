n = int(input())
num = list(map(int, input().split()))
num.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1

for i in range(2, n+1):
    maxNum = 0
    for j in range(i-1, 0, -1):
        if num[j] < num[i] and dy[j] > maxNum:
            maxNum = dy[j]
    dy[i] = maxNum + 1

print(max(dy))