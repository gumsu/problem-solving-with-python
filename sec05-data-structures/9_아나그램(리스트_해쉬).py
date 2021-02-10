import sys

for i in range(1, 6):
    sys.stdin = open(f'in{i}.txt', "rt")

    a = input()
    b = input()

    str1 = [0]*52
    str2 = [0]*52

    # 대문자는 0~25 소문자는 26~51까지 배치할 예정
    # 아스키코드: 대문자는 65~ 소문자는 97~
    for x in a:
        if x.isupper():
            str1[ord(x)- 65] += 1
        else:
            str1[ord(x) -71] += 1
    
    for x in b:
        if x.isupper():
            str2[ord(x)- 65] += 1
        else:
            str2[ord(x) -71] += 1
    
    for i in range(52):
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("YES")