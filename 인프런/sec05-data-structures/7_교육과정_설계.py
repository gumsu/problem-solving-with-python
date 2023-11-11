import sys
from collections import deque

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    need = input()
    n = int(input())
    for x in range(n):
        plan = input()
        dq = deque(need)

        for y in plan: 
            if y in dq:  # y라는 과목이 큐안에 들어있다면(필수 과목이라면)
                if y != dq.popleft():    # y라는 과목이 큐의 첫번째 요소가 아니라면(필수 과목 순서를 지키지 않았다면)
                    print(f'#{x+1} NO')
                    break
        else:   # for문이 다 끝났더라도(필수 과목 순서를 다 지켰더라도)
            if len(dq) == 0:
                print(f'#{x+1} YES')
            else:
                print(f'#{x+1} NO') # 큐안에 요소가 남아있다면(필수 과목을 다 듣지 않았을 때)