import sys

def outputNum(num, i):
    outputTxt = f'out{i}.txt'
    sys.stdin = open(outputTxt, "rt")
    result = int(input())
    if num == result:
        return print("정답입니다!")
    else:
        return print("오답입니다.")

def sol():
    for i in range(1,6):
        inputTxt = f'in{i}.txt'
        sys.stdin = open(inputTxt, "rt")
        n, k = map(int, input(f"{i}번째 데이터를 입력하였습니다: \n").split())
        numList = list(map(int, input(f"{i}번째 카드값을 입력하였습니다: ").split()))
        numSet = set()
        for j in range(n):
            for x in range(j+1, n):
                for z in range(x+1 , n):
                    numSet.add(numList[j]+numList[x]+numList[z])
        numList = list(numSet)
        numList.sort(reverse=True)
        outputNum(numList[k-1], i)

sol()