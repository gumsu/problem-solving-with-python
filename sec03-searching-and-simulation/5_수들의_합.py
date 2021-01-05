import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt',"rt")

    n, m = map(int,input().split())
    numList = list(map(int, input().split()))

    cnt = 0
    lt = 0
    rt = 1
    total = numList[lt]

    while lt < n:

        if total < m:
            if rt < n:
                total += numList[rt]
                rt += 1
            else:
                break
        elif total == m:
            cnt += 1
            total -= numList[lt]
            lt += 1
        else:
            total -= numList[lt]
            lt += 1
    
    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == cnt:
        print(f'{cnt} -> 정답입니다 ')
    else:
        print("오답입니다")