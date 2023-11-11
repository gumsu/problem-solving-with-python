# 퀵정렬 (분할해서 합치기) 전위순회방식, 피봇사용
def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)
        

if __name__=="__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print(f"Before sort: {arr}")
    Qsort(0,9)
    print(f"After sort: {arr}")