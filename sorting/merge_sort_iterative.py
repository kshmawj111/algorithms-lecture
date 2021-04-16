num_iter = 0


def iterative_merge(A, left, mid, right):
    N = right - left + 1
    n1 = mid-left + 1
    n2 = right - mid

    L = A[left:left+n1] + [float('inf')] # index overflow를 방지하며 더 이상 해당 배열의 인덱스를 움직이지 않게 해주는 일종의 트릭
    R = A[mid+1:mid+1+n2] + [float('inf')]
    i, j = 0, 0     # L, R list index

    global num_iter
    # 비교 하면서 원본 배열에 바로 값을 집어 넣음
    for k in range(left, left+N): # k for origina list index
        num_iter += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1

        else:
            A[k] = R[j]
            j += 1



def merge_sort_iter(ary: list):
    size, i = 1, 0
    length = len(ary)

    while size < length:
        left = 0

        while left < length: # mergesort 하고자 하는 subarray의 범위를 계산함
            mid = min(left + size - 1, length-1) # 인덱스 오버플로우 방지
            right = min(left + 2*size - 1, length-1) # right 인덱스를 포함하여 mergesort 실행할 것임
            iterative_merge(ary, left, mid, right)
            left += 2*size  # 다음 subarray의 시작 지점으로 다시 재할당
                            # size=4이면 0에서 시작했다면 4부터 8까지를 다음 sub array로 지정하기 위해

        size *= 2 # 사이즈는 두배씩 커지도록
    return ary


if __name__ == '__main__':
    a = [8, 7, 6, 5, 4, 3, 2, 1]
    print(merge_sort_iter(a))
    print(num_iter)
