import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    num, m = map(int, input().split())
    # num 리스트에 있는 숫자를 string으로 변환한 후, 다시 int형으로 바꾸어 리스트에 넣는다.
    num = list(map(int, str(num)))

    stack = list()

    for x in num:
        while stack and m > 0 and stack[-1] < x: 
            stack.pop()
            m -= 1
            #stack이 비어있지 않고, m이 0보다 크고, stack의 제일 마지막 자료가 x보다 작을때
            # 계속 꺼낸다
        stack.append(x) # 내 앞에 작은 숫자를 다 뺐다면, x를 넣는다.
        
    if m != 0:
        stack = stack[:-m]
    res = ''.join(map(str, stack))
    
    sys.stdin = open(f'out{i}.txt', "rt")
    out = input()
    if out == res:
        print(f"{res} -> 정답입니다")
    else:
        print("오답입니다")
