import itertools as it

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
# a개의 리스트에서 k개를 뽑아 조합을 만들어 줌
for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)