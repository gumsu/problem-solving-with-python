import sys

#상태트리
for i in range(1,6):
    sys.stdin = open(f'in{i}.txt',"rt")

    def DFS(L, sum):
        global switch
        if switch: return
        if sum > total//2:
            return
        if L == n:
            if sum == (total-sum):
                print("YES")
                #sys.exit(0)     # 함수의 종료 X, 프로그램의 종료 O
                switch = 1
        else:
            DFS(L+1, sum+a[L])  # 원소 포함할 때
            DFS(L+1, sum)       # 원소 포함하지 않을 때
            
    if __name__ == "__main__":
        switch = 0
        n = int(input())
        a = list(map(int, input().split()))
        total = sum(a)
        DFS(0, 0)
        if switch==0: print("NO") # DFS()함수 내부에 있는 프로그램이 종료 안되면 실행된다.