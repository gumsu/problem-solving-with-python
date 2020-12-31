import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    testCase = int(input())
    for j in range(testCase):
        n, s, e, k = map(int, input().split())
        numList = list(map(int, input().split()))
        numList = numList[s-1:e]
        numList.sort()
        print(f'#{j+1} {numList[k-1]}')
    print("----")