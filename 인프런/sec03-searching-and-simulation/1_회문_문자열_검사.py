import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")
    arr = [input() for _ in range(int(input()))]

    cnt = 0
    for i in arr:
        cnt += 1
        i = i.upper()   # 들어오는 문자를 모두 대문자로 변경

        # 1번째 방법
        if i == i[::-1]:
            print(f'#{cnt} YES')
        else:
            print(f'#{cnt} NO')

        # 2번째 방법
        '''
        reverseStr = ''.join(reversed(i))
        if reverseStr == i:
            print(f'#{cnt} YES')
        else:
            print(f'#{cnt} NO')
        '''

        # 3번째 방법
        '''
        size = len(i)
        for j in range(size//2):
            if i[j] != i[-1-j]:     # 앞에 인덱스, 뒤에 인덱스 비교
                print(f'#{cnt} NO')
                break
        else:
            print(f'#{cnt} YES')
    print('==============')
    '''