import sys
from collections import deque

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n, m = map(int, input().split())
    emergency = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
    emergency = deque(emergency)
    cnt = 0

    while True:
        current = emergency.popleft()   #(0, 60)
        if any(current[1] < x[1] for x in emergency):
            emergency.append(current)
        else:
            cnt += 1
            if current[0] == m:
                break

    sys.stdin = open(f'out{i}.txt', "rt")

    out = int(input())

    if out == cnt:
        print(f"{cnt} -> 정답입니다")
    else:
        print("오답입니다")