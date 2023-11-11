import sys

for i in range(1,6):
    inputTxt = f'in{i}.txt'
    sys.stdin = open(inputTxt, "rt")
    n = int(input("데이터를 입력하였습니다: "))
    numList = map(int, input().split())

    def digit_sum(x):
        sum = 0

        while x > 0:
            sum += x % 10
            x = x // 10
        return sum

    max = -2147000000

    for x in numList:
        tot = digit_sum(x)

        if tot > max:
            max = tot
            res = x
    
    sys.stdin = open(f'out{i}.txt', "rt")
    outNum = int(input())

    if outNum == res:
        print(f"{res} -> 정답입니다")
    else:
        print("오답입니다")