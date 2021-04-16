"""
    Quick sort partitioning the array into 3 parts.
    Reference to Dijkstra's 3-way partitioning

    1) less than pvt
    2) equal to pvt
    3) greater than pvt

    for 2), we don't need to sort them because they are already sorted.

"""
import math
from copy import copy
from random import randint

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


def quick_sort_3way(l, p, r, verbose=False):
    if p<r:
        lp, rp = partition(l, p, r, verbose=verbose)
        quick_sort_3way(l, p, lp - 1) # left
        quick_sort_3way(l, rp + 1, r) # right
    return l


def partition(l, p, r, verbose=False):
    global num_iter
    pivot = l[randint(p, r)] # randomized pivots
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
    iterations = []

    for _ in range(100):
        a = [randint(0, 5) for _ in range(1000)]
        quick_sort_3way(a, 0, len(a) - 1, verbose=False)
        iterations.append(num_iter)

    print(sum(iterations)/len(iterations))
