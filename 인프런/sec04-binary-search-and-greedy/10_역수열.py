import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n = int(input())
    sequence = list(map(int, input().split()))

    new = [0]*n

    for x in range(n):
        cnt = 0
        for y in range(n):
            if new[y] == 0:
                cnt += 1
            if cnt == sequence[x]+1:
                new[y] = x+1
                break
        
    print(*new)