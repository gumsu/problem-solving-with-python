import sys

for i in range(1,6):
    inputTxt = f'in{i}.txt'
    sys.stdin = open(inputTxt, "rt")
    n = int(input("데이터를 입력하였습니다: "))
    numList = map(int, input().split())

    def reverse(x):
        length = len(str(x))
        reverseNum = 0

        while x > 0:
            num = x % 10
            x = x // 10

            reverseNum += num * (10**(length-1))
            length -= 1
        return reverseNum

    def isPrime(x):
        
        if x == 1:
            return False
        elif x == 2:
            return True
        
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    
    for j in numList:
        if isPrime(reverse(j)) == True:
            print(reverse(j), end =' ')
    print()