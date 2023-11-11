import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    arr = [list(map(int, input().split())) for _ in range(7)]

    cnt = 0

    for x in range(7):
        for y in range(3):
            tmp = arr[x][y:y+5]
            if tmp == tmp[::-1]:
                cnt += 1
            
            tmp = list()
            for z in range(5):
                tmp.append(arr[y+z][x])
            if tmp == tmp[::-1]:
                cnt += 1

    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == cnt:
        print(f'{cnt} -> 정답입니다!')
    else:
        print("오답입니다")