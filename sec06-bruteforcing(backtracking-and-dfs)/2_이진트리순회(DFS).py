import sys

#sys.stdin = open(f'input.txt',"r")

def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')    # 함수 본연의 일(나의 할일을 먼저 수행하고 자식노드로 이동) -> 전위순회
        DFS(v*2)    # 왼쪽 자식노드
        DFS(v*2+1)  # 오른쪽 자식노드

        # 함수 본연의 일을 자식노드 사이에 넣는다면 중위순회
        # 함수 본연의 일을 자식노드 이후에 넣는다면 후위순회

if __name__ == "__main__":
    DFS(1)