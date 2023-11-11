import sys

for z in range(1, 6):
    sys.stdin = open(f'in{z}.txt', "rt")

    def check(a):
        for x in range(9):
            ch1 = [0]*10
            ch2 = [0]*10
            for y in range(9):
                ch1[a[x][y]] = 1
                ch2[a[y][x]] = 1
            if sum(ch1) != 9 or sum(ch2) != 9:
                return False
        
        # i, j는 9개의 그룹을 나누는 반복문
        # k, s는 하나의 그룹 안에 9개의 칸을 도는 반복문이다.
        for i in range(3):
            for j in range(3):
                ch3 = [0]*10
                for k in range(3):
                    for s in range(3):
                        ch3[a[i*3+k][j*3+s]] = 1
                if sum(ch3) != 9:
                    return False
        return True

    a = [list(map(int, input().split())) for _ in range(9)]

    if check(a):
        print("YES")
    else:
        print("NO")