import sys

def inputNum():
    for i in range(1,6):
        inputTxt = f'in{i}.txt'
        sys.stdin = open(inputTxt, "rt")
        n, m = map(int,(input("데이터를 입력하였습니다: ")).split())
        sol(n, m, i)


def sol(n, m, i):
    pol1 = list(range(1,n+1))
    pol2 = list(range(1,m+1))

    countList = [0]*len(pol1)*len(pol2)
    maxNum = 0
    
    for x in pol1:
        for y in pol2:
            countList[x+y] += 1

    for i in range(n+m+1):
        if countList[i] > maxNum:
            maxNum = countList[i]
    for i in range(n+m+1):
        if countList[i] == maxNum:
            print(i, end = ' ')
    print()
    
inputNum()