import sys
from collections import deque

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n, k = map(int, input().split())
    dq = list(range(1, n+1))
    dq = deque(dq)  # 리스트를 덱으로 자료구조 변환
    
    while dq:
        for _ in range(k-1):
            current = dq.popleft()
            dq.append(current)
        dq.popleft()

        if len(dq) == 1:
            res = dq[0]
            dq.popleft()
    
    sys.stdin = open(f'out{i}.txt', "rt")

    out = int(input())

    if out == res:
        print(f"{res} -> 정답입니다")
    else:
        print("오답입니다")