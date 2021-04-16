from copy import copy
from random import randint

num_iter = 0

def quick_select(l, p, r, k):
    k -= 1
    li = partition(l, p, r)
    if li == k:
        return l[li]

    elif li > k:
        quick_select(l, p, li-1, k)

    elif li < k:
        quick_select(l, li+1, r, k)


def quick_sort(l, p, r):
    if p<r:
        pivot_index = partition(l, p, r)
        quick_sort(l, p, pivot_index-1)
        quick_sort(l, pivot_index+1, r)
    return l


def partition(l, p, r):
    global num_iter
    pi = randint(p, r)
    pivot = l[pi]
    l[pi], l[p] = l[p], l[pi]

    i = p+1
    for j in range(i, r+1):
        num_iter += 1
        if l[j] < pivot:
            l[i], l[j] = l[j], l[i]
            i += 1

    l[i-1], l[p] = l[p], l[i-1]
    return i-1 # return pivot's index


if __name__ == '__main__':
    a = [3,2,1,5,8,4,7,6]
    quick_sort(a, 0, len(a)-1)
    print(a)
