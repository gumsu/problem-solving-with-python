import sys

for i in range(1,6):
    inputTxt = f'in{i}.txt'
    sys.stdin = open(inputTxt, "rt")
    n = int(input("데이터를 입력하였습니다: "))

    maxMoney = 0
    for j in range(n):
        tmp = input().split()
        tmp.sort()
        a, b, c = map(int, tmp)

        if a == b == c:
            money = 10000 + a* 1000
        elif a == b or a == c:
            money = 1000 + (a*100)
        elif b == c:
            money = 1000 + (b*100)
        else:
            money = c*100

        if money > maxMoney :
            maxMoney = money
    
    sys.stdin = open(f'out{i}.txt', "rt")
    outNum = int(input())

    if outNum == maxMoney:
        print(f'{maxMoney} -> 정답입니다')
    else:
        print('오답입니다')
