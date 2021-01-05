import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    total = 0
    s = e = n//2

    for x in range(n):
        for y in range(s, e+1):
            total += arr[x][y]
        
        if x < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    
    sys.stdin = open(f'out{i}.txt',"rt")
    out = int(input())

    if out == total:
        print(f'{total} -> 정답입니다 ')
    else:
        print(f"{total} -> 오답입니다")
