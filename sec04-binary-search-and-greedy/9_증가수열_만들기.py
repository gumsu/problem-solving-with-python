import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n = int(input())
    sequence = list(map(int, input().split()))

    lt = 0
    rt = n-1
    last = 0
    res = ""
    tmp = []

    while lt <= rt:
        if sequence[lt] > last:
            tmp.append((sequence[lt], 'L'))
        if sequence[rt] > last:
            tmp.append((sequence[rt], 'R'))
        
        tmp.sort()
        
        if len(tmp) == 0:
            break
        else:
            res = res + tmp[0][1]
            last = tmp[0][0]
            if tmp[0][1] == 'L':
                lt += 1
            else:
                rt -= 1
        tmp.clear()
    
    print(len(res))
    print(res)