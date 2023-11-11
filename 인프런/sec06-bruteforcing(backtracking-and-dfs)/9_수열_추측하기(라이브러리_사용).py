import itertools as it

n, f = map(int, input().split())
b = [1]*n
cnt = 0

for i in range(1, n):
    b[i] = b[i-1]*(n-i)/i
a = list(range(1, n+1))

# a의 모든 수열을 구해준다. (4, 3) -> 1~4까지 중 3개를 뽑아 만들 수 있는 모든 경우의 수를 구해준다.
for tmp in it.permutations(a):
    sum = 0
    for idx, x in enumerate(tmp):
        sum += (x * b[idx])
    if sum == f:
        for x in tmp:
            print(x, end = ' ')
        break