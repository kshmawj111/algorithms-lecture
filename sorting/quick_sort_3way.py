"""
    Quick sort partitioning the array into 3 parts.
    Reference to Dijkstra's 3-way partitioning

    1) less than pvt
    2) equal to pvt
    3) greater than pvt

    for 2), we don't need to sort them because they are already sorted.

"""
from utils.shuffle import shuffle

num_iter = 0


def quick_select(l, p, r, k):
    answer = None
    li, ri = partition(l, p, r)
    if li == k:
        answer = l[li]

    elif ri == k:
        answer = l[ri]

    elif li > k:
        answer = quick_select(l, p, ri-1, k)

    elif li < k:
        answer = quick_select(l, li+1, r, k)

    return answer


def quick_sort_3way(l, p, r):
    if p<r:
        lp, rp = partition(l, p, r)
        quick_sort_3way(l, p, lp - 1)
        quick_sort_3way(l, rp + 1, r)
    return l


def partition(l, p, r, verbose=False):
    global num_iter
    pivot = l[(p+r)//2]
    lp, rp = p, r
    i = p

    while i <= rp:
        num_iter += 1
        if l[i] < pivot:
            l[lp], l[i] = l[i], l[lp]
            lp += 1
            i += 1

        elif l[i] == pivot:
            i += 1

        elif l[i] > pivot:
            l[rp], l[i] =l[i], l[rp]
            rp -= 1

    if verbose:
        print(l, end=' ')
        print(f'lp: {lp}, rp: {rp}', end=' ')
        print(f'pivot: {pivot}')
    return lp, rp # return pivot's index


if __name__ == '__main__':
    a = [5,8,4,6,2,3,1,1,2,5,6,8,6,4,5,8,9,6,2,1,3,2,5,6,2,3,4,5,4,6,4]
    print(quick_sort_3way(a, 0, len(a) - 1))
    print(num_iter)

    a = [3,2,1,2,5,3,65,3,5,4,203,2,12,12,2,33,52,53,2,5,23,6,523,]
    a = shuffle(a)
    print(quick_select(a, 0, len(a) - 1,14))