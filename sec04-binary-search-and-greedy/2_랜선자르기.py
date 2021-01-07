import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    k, n = map(int, input().split())

    cable = [int(input()) for _ in range(k)]

    lt = 1
    rt = max(cable)
    longest = 0

    while lt <= rt:
        cnt = 0
        mid = (lt + rt) // 2
        for x in cable:
            cnt += x // mid
        
        if cnt >= n:
            longest = mid
            lt = mid + 1
        else:
            rt = mid - 1
    
    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == longest:
        print(f'{longest} -> 정답입니다')
    else:
        print('오답입니다')