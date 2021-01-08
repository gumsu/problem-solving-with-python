import sys

for i in range(1,6):
    sys.stdin = open(f'in{i}.txt', "rt")

    n = int(input())

    applicants = [list(map(int, input().split())) for _ in range(n)]

    # 키가 큰 순 정렬
    applicants.sort(reverse= True)

    cnt = 0
    largest = 0

    # 키는 이미 크기 때문에 몸무게만 비교해준다.
    # 최대값을 갱신해주면서 나보다 키 큰 사람들만 몸무게로 이길수 있는지 비교해준다.
    for height, weight in applicants:
        if weight > largest:
            largest = weight
            cnt += 1

    sys.stdin = open(f'out{i}.txt', "rt")

    out = int(input())

    if out == cnt:
        print(f'{cnt} -> 정답입니다!')
    else:
        print("오답입니다")