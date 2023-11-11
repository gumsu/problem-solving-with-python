''' 전역변수와 지역변수 '''

def DFS1():
    cnt = 3
    print(cnt)          # 함수의 지역변수에 존재하는가? 있으면 지역변수로 사용

def DFS2():
    global cnt          # 함수 내에 cnt는 모두 전역변수로 사용한다.
    if cnt == 5:
        cnt = cnt+1     # cnt가 지역변수로 선언되면서 함수 내에 존재하는 cnt는 모두 지역변수로 변화
        print(cnt)      # 함수의 지역변수에 존재하는가? 없으면 전역변수로 사용

if __name__ == "__main__":
    cnt = 5             # 전역변수는 모든 함수가 다 접근 가능(공용)
    DFS1()
    DFS2()
    print(cnt)          # DFS2에서 6으로 변화한 cnt 출력