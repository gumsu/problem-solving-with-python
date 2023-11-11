import sys



for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    arr = [list(map(int, input().split())) for _ in range(int(input()))]

    maxSum = -2147000000

    for x in range(len(arr)):
        row = col = 0
        for y in range(len(arr)):
            row += arr[x][y]
            col += arr[y][x]
        
        if row > maxSum:
            maxSum = row
        if col > maxSum:
            maxSum = col
    
    diag1 = diag2 = 0
    for x in range(len(arr)):
        diag1 += arr[x][x]
        diag2 += arr[x][len(arr)-1-x]
    
    if diag1 > maxSum:
        maxSum = diag1
    if diag2 > maxSum:
        maxSum = diag2

    sys.stdin = open(f'out{i}.txt', "rt")
    out = int(input())

    if out == maxSum:
        print(f'{maxSum} -> 정답입니다!')
    else:
        print(f"{maxSum} 오답입니다 \n {out}")