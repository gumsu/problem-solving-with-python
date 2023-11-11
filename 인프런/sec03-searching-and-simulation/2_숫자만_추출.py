import sys
for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")
    a = input()

    res = 0
    for i in a:
        if i.isdecimal():
            res = res * 10 + int(i)
    
    print(res)
    cnt = 0
    for i in range(1, res+1):
        if res % i ==0:
            cnt += 1
    print(cnt)
    '''
    numList = [str(i) for i in range(10)]
    num = str()

    for i in a:
        if i in numList:
            num += i
    num = int(num)

    cnt = 1
    for i in range(1, num//2+1):
        if num % i == 0:
            cnt +=1
    print(num)
    print(cnt)
    print('===============')
    '''