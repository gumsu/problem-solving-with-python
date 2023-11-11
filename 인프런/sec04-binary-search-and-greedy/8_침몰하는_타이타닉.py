import sys
from collections import deque

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n, m = map(int, input().split())
    weight = list(map(int, input().split()))

    # 가장 무거운 순으로
    weight.sort(reverse=True)
    cnt = 0

    # 리스트를 덱으로 변경
    weight = deque(weight)

    while True:
        if not weight:
            break
        if len(weight) == 1:
            cnt += 1
            break
        if weight[0] + weight[-1] > m:
            weight.popleft()    # 덱은 popleft()를 사용하여 맨 앞의 요소를 뺀다.
            cnt += 1
        elif weight[0] + weight[-1] <= m:
            weight.pop()
            weight.popleft()    # 덱은 popleft()를 사용하여 맨 앞의 요소를 뺀다.
            cnt += 1
    
    '''
    # 리스트를 사용하여 맨 앞의 요소를 pop하면 자동으로 다음 인덱스의 요소들이 한 칸씩 땡겨온다
    -> 매우 비효율적이므로 deque를 사용한다.
    while True:
        if not weight:
            break
        if len(weight) == 1:
            cnt += 1
            break
        if weight[0] + weight[-1] > m:
            weight.pop(0)
            cnt += 1
        elif weight[0] + weight[-1] <= m:
            weight.pop()
            weight.pop(0)
            cnt += 1
    '''
    
    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == cnt:
        print(f'{cnt} -> 정답입니다!')
    else:
        print(f"{cnt} -> 오답입니다!")