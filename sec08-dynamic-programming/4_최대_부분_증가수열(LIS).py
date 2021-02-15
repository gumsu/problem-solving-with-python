n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy = [0]*(n+1)  # 증가 수열의 최대값, dy[2]는 arr[2]까지 수열에서 증가 수열의 최대값을 말한다.
dy[1] = 1

for i in range(2, n+1):
    print(*dy)
    maxNum = 0
    for j in range(i-1, 0, -1): # 거꾸로 가면서 찾기
        if arr[j] < arr[i] and dy[j] > maxNum:
            maxNum = dy[j]
    dy[i] = maxNum + 1

print(max(dy))