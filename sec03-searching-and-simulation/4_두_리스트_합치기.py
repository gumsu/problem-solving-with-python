import sys

for i in range(1, 6):

    sys.stdin = open(f'in{i}.txt', "rt")

    n = int(input())
    nList = list(map(int, input().split()))
    m = int(input())
    mList = list(map(int, input().split()))

    # 1번째 방법
    p1 = p2 = 0     #포인터 변수 초기화
    newList = list()

    # 아무 포인터 변수나 먼저 끝나면 while문 종료
    while p1 < n and p2 < m:
        if nList[p1] < mList[p2]:
            newList.append(nList[p1])
            p1 += 1
        else:
            newList.append(mList[p2])
            p2 += 1
    
    # 끝까지 가지 못한 리스트의 남은 값들을 합쳐준다.
    if p1 < n:
        newList = newList + nList[p1:]
    else:
        newList = newList + mList[p2:]

    '''
    # 2번째 방법

    newList = nList + mList
    newList.sort()
    '''

    sys.stdin = open(f'out{i}.txt', "rt")
    res = list(map(int, input().split()))

    if res == newList:
        print(f'{newList} \n => 정답입니다')
    else:
        print("\n 오답입니다")