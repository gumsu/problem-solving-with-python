import sys

def start():
    inputNum()

def inputNum():
    for i in range(1,6):
        inputTxt = f'in{i}.txt'
        sys.stdin = open(inputTxt, "rt")
        n, k = map(int,(input(f"{i}번째 데이터를 입력하였습니다: ")).split())
        sol(n, k, i)

def outputNum(num, i):
    outputTxt = f'out{i}.txt'
    sys.stdin = open(outputTxt, "rt")
    result = int(input())
    if num == result:
        return print("정답입니다!")
    else:
        return print("오답입니다.")

def sol(n, k, j):
    numList = []
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            numList.append(i)

    if len(numList) < k:
        return outputNum(-1, j)
    else:
        minNum = numList[k-1]
        return outputNum(minNum, j)

start()