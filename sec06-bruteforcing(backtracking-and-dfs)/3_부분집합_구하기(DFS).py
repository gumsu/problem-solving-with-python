import sys

#상태트리
for i in range(1,6):
    sys.stdin = open(f'in{i}.txt',"rt")

    def DFS(v):
        if v == n+1:        # 종착지(DFS(4)가 나오면 멈추고 위로 back)
            for i in range(1, n+1):
                if ch[i] == 1:
                    print(i, end=' ')
            print()
        else:               # 사용한다, 하지 않는다 (check 리스트를 사용함)
            ch[v] = 1
            DFS(v+1)
            ch[v] = 0
            DFS(v+1)
            
    if __name__ == "__main__":
        n = int(input())
        ch = [0]*(n+1)
        DFS(1)