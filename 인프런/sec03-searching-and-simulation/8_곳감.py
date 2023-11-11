import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")
    n = int(input())
    persimmon = [list(map(int,input().split())) for _ in range(n)]

    m = int(input())
    for _ in range(m):
        h, t, k = map(int, input().split())
        if t == 0:
            for _ in range(k):
                tmp = persimmon[h-1].pop(0)
                persimmon[h-1].append(tmp)
        else:
            for _ in range(k):
                tmp = persimmon[h-1].pop()
                persimmon[h-1].insert(0, tmp)
    
    s = 0
    e = n - 1
    total = 0
    for x in range(n):
        for y in range(s, e+1):
            total += persimmon[x][y]

        if x < n//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1
    
    sys.stdin = open(f'out{i}.txt',"rt")
    out = int(input())

    if out == total:
        print(f'{total} -> 정답입니다!')
    else:
        print(f'{total} -> 오답입니다!')