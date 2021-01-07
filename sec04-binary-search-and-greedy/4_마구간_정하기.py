import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    def Count(len):
        cnt = 1
        ep = stables[0]
        for x in range(1, n):
            if stables[x] - ep >= len:
                cnt += 1
                ep = stables[x]
        return cnt            

    n, c = map(int, input().split())

    stables = [int(input()) for _ in range(n)]

    stables.sort()

    lt = 1
    rt = stables[n-1]

    while lt <= rt:
        mid = (lt + rt) // 2

        if Count(mid) >= c: # 가장 가까운 두 말의 거리
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)