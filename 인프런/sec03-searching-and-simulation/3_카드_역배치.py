import sys

for i in range(2, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    cardList = [ i for i in range(21)]
    
    # 1번째 방법
    for _ in range(10):
        a, b = map(int, input().split())

        for j in range((b-a+1)//2):
            cardList[a+j], cardList[b-j] = cardList[b-j], cardList[a+j]
    
    '''
    # 2번째 방법
    for _ in range(10):
        a, b = map(int, input().split())
        
        tmp = cardList[a: b+1]
        tmp = tmp[::-1]
        cardList[a: b+1] = tmp
    '''
    cardList.pop(0)
    print(cardList)

    sys.stdin = open(f'out{i}.txt',"rt")
    out = list(map(int, input().split()))

    if out == cardList:
        print(f'{cardList} \n => 정답입니다!')
    else:
        print("오답입니다")