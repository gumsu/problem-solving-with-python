import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    dx = [-1, 0 ,1, 0]
    dy = [0, 1, 0 ,-1]
    
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.insert(0, [0]*n)
    arr.append([0]*n)

    for j in arr:
        j.insert(0, 0)
        j.append(0)
    
    cnt = 0

    for x in range(1, n+1):
        for y in range(1, n+1):
            if all(arr[x][y] > arr[x+dx[k]][y+dy[k]] for k in range(4)) :
                cnt += 1

    sys.stdin = open(f'out{i}.txt',"rt")
    out = int(input())

    if out == cnt:
        print(f'{cnt} -> 정답입니다!')
    else:
        print(f'{cnt} -> 오답입니다')