n = int(input())
p = dict()
for _ in range(n):
    word = input()
    p[word] = 1

# 사용된 단어는 0으로 체크
for i in range(n-1):
    word=input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)