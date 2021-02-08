# 병합정렬 (반으로 나누어서 정렬하고 합치기) 후위순회방식
def Dsort(lt, rt):
    if lt < rt:
        mid = (lt+rt)//2
        Dsort(lt, mid)
        Dsort(mid+1, rt)

        # 두 갈래를 다 뻗고난 후에 (자식노드의 업무가 다 끝나고 나서)
        # 본연의 업무 - 정렬된 두 영역을 병합해준다. (후위순회)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1
        if p1 <= mid: # p2 쪽이 다 들어가고 끝났을 때(아직 p1에는 남아있음)
            tmp = tmp+arr[p1:mid+1]
        if p1 <= mid: # p1 쪽이 다 들어가고 끝났을 때(아직 p2에는 남아있음)
            tmp = tmp+arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]

if __name__=="__main__":
    arr = [12, 11, 45, 36, 15, 67, 33, 21]
    print(f"Before sort: {arr}")
    Dsort(0, 7)
    print(f"After sort: {arr}")