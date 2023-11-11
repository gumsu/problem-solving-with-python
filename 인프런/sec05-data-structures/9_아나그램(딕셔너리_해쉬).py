import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    a = input()
    b = input()

    str1 = dict()
    str2 = dict()

    for x in a:
        # x라는 키가 있다면 x키의 value를 리턴해서 값을 +1해준다, 키가 없다면 0을 리턴
        str1[x] = str1.get(x, 0) + 1
    for x in b:
        str2[x] = str2.get(x, 0) + 1
    
    for i in str1.keys():
        if i in str2.keys():
            if str1[i] != str2[i]:
                print("NO")
                break
        else:
            print("NO")
            break
    else:
        print("YES")
