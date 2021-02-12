# 이미 나온 값은 dy 리스트에 저장해두고 사용한다. - 메모이제이션
def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))