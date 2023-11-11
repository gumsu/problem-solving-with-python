import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    l = int(input())
    width = list(map(int, input().split()))
    m = int(input())

    # 매번 정렬하면서 끝 값(가장 큰 값)+1 과 처음 값(가장 작은 값)-1을 반복
    for _ in range(m):
        width.sort()
        width[0] = width[0] + 1
        width[l-1] = width[l-1] - 1
    
    # 마지막으로 또 정렬 해주어야 함
    width.sort()
    res = width[l-1] - width[0]

    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == res:
        print(f'{res} -> 정답입니다!')
    else:
        print(f"{res} -> 오답입니다!")