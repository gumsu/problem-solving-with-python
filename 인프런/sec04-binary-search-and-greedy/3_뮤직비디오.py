import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    def Count(capacity):
        cnt = 1
        dvd = 0
        for x in minutes:
            if dvd + x > capacity:
                cnt += 1
                dvd = x
            else:
                dvd += x
        return cnt

    n, m = map(int ,input().split())
    minutes = list(map(int, input().split()))
    maxx = max(minutes)

    lt = 1
    rt = sum(minutes)
    res = 0

    while lt <= rt:
        mid = (lt + rt) // 2
        dvd = 0
        cnt = 1
        if mid >= maxx and Count(mid) <= m:
            res = mid
            rt = mid - 1
        else:
            lt = mid + 1
    print(res)