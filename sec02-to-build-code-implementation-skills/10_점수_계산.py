import sys

for i in range(1,6):
    inputTxt = f'in{i}.txt'
    sys.stdin = open(inputTxt, "rt")
    n = int(input("데이터를 입력하였습니다: "))
    score = list(map(int, input().split()))

    sum = 0
    cnt = 0

    for j in score:
        if j == 1:
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    
    sys.stdin = open(f'out{i}.txt', "rt")
    outNum = int(input())

    if outNum == sum:
        print(f'{sum} -> 정답입니다!')
    else:
        print('오답입니다')