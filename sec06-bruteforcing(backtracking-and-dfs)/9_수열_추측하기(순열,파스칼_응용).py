import sys
def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0) # 최초의 답이 나오면 프로그램 종료
    for i in range(1, n+1):
        if check[i] == 0:
            p[L] = i
            check[i] = 1
            DFS(L+1, sum + (p[L]*b[L]))
            check[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0]*n   # 순열 만드는 배열
    b = [1]*n   # 1234,1243, ... 파스칼의 삼각형의 맨 끝 배열은 무조건 1이다. -> 1로 초기화
    # 이항 계수 (x+1)^2 = 2C0 2C1 2C2    (x+1)^3 = 3C0 3C1 3C2 3C3  -> 형태로 만들어줘야 한다.
    check = [0]*(n+1)   # 중복방지 체크
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)