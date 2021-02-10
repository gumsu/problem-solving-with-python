import heapq as hq

# 최소힙: 부모가 자식 노드보다 항상 작아야한다.
a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a)) # 루트 노드값 출력
    else:
        hq.heappush(a, n) # a리스트에 n을 넣는다.