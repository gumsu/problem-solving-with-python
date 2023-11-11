import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    a = input()
    stack = list()
    res = ''

    for x in a:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] =='*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x =='-':
                while stack and stack[-1]!= '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1]!= '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()
    
    sys.stdin = open(f'out{i}.txt', "rt")

    out = input()

    if out == res:
        print("정답입니다")
    else:
        print("오답입니다")