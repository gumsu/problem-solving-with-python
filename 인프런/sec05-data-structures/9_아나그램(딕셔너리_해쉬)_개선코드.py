import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    a = input()
    b = input()

    sh = dict()

    for x in a:
        sh[x] = sh.get(x, 0) + 1
    
    for x in b:
        sh[x] = sh.get(x, 0) - 1

    for x in a:
        if sh.get(x) > 0:
            print("NO")
            break
    else:
        print("YES")