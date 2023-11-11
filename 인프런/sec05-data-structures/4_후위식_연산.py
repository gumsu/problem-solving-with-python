import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    a = input()
    stack = list()
    res = ''

    for x in a:
        if x.isdecimal():
            stack.append(int(x))
        else:
            if x == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2+n1)
            elif x == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2-n1)
            elif x == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2*n1)
            elif x == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2/n1)
    res = stack[0]
    print(res)

    sys.stdin = open(f'out{i}.txt', "rt")

    out = int(input())

    if out == res:
        print("정답입니다")
    else:
        print("오답입니다")