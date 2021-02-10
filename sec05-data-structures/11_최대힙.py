import heapq as hq

# 최대힙: 부모가 자식노드보다 항상 커야한다.
# 최소힙에서 부호만 -로 바꾸어준다.
a =[]

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)