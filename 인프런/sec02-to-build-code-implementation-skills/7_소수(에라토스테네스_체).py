import sys

for i in range(1,6):
    inputTxt = f'in{i}.txt'
    sys.stdin = open(inputTxt, "rt")
    n = int(input("데이터를 입력하였습니다: "))

    numList = [0]*(n+1)
    numList[0] = 1
    numList[1] = 1
    cnt = 0
    for x in range(2,n+1):
        if len(numList) == 2:
            cnt = 1
        elif numList[x] == 0:
            cnt += 1
            for y in range(x, n+1, x):
                    numList[y] = 1

    print(cnt)