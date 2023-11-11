import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n = int(input())

    start_end = [list(map(int, input().split())) for _ in range(n)]

    # 회의가 끝나는 시간을 기준으로 정렬 (2번째 인자로 비교하여 정렬)
    # 만약 첫 번째 값이 동일하다면 두 번째 값을 비교하여 정렬
    start_end.sort(key=lambda x: (x[1], x[0]))

    meeting = start_end[0]
    cnt = 1

    for x, y in start_end:
        if meeting[1] == x:
            meeting = [x, y]
            cnt += 1
        elif meeting[1] < x:
            meeting = [x, y]
            cnt += 1
    
    sys.stdin = open(f'out{i}.txt', "rt")

    out = int(input())

    if out == cnt:
        print(f'{cnt} ->  정답입니다! ')
    else:
        print('오답입니다')