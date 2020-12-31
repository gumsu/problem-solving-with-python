import sys

def outputNum(x, y, z):
    sys.stdin = open(f'out{z}.txt', "rt")
    result = list(map(int, input().split()))
    myAnswer = list()
    myAnswer.append(x)
    myAnswer.append(y)
    
    if result == myAnswer:
        return print("정답입니다!")
    else:
        return print("오답입니다!")
        
for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")
    n = int(input(f"{i}번째 테스트 케이스: n명의 학생이 입력됩니다."))
    scoreList = list(map(int, input().split()))
    avg = round(sum(scoreList)/n)
    minNum = 999999999
    score = 0
    student = 0

    for idx, x in enumerate(scoreList):
        tmp = abs(x - avg)
        if tmp < minNum:
            minNum = tmp
            score = x
            student = idx + 1
        elif tmp == minNum:
            if x > score:
                score = x
                student = idx + 1
            
    outputNum(avg, student, i)
    #print(avg, student)