# 중복 허용 X, 뒤에서부터 넣으면 중복을 방지할 수 있다.
n, m = map(int, input().split())
dy = [0]*(m+1)

for i in range(n):
    score, time = map(int, input().split())
    print(*dy)
    for j in range(m, time-1, -1):
        dy[j] = max(dy[j], dy[j-time]+score)

print(dy[m])