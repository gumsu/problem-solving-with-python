import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    laser = input()

    stack = list()
    cnt = 0

    for x in range(len(laser)):
        if laser[x] == '(':
            stack.append(x)
        else:
            stack.pop()
            if laser[x-1] == '(':
                cnt += len(stack)
            else:
                cnt +=1
    
    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == cnt:
        print(f'{cnt} -> 정답입니다! ')
    else:
        print(f'{cnt} -> 오답입니다 \n {out}')