num_iter = 0


def merge(left: list, right: list):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(ary, left, right):
    if left < right:
        mid = (left + right) // 2   # divide
        l = merge_sort(ary, left, mid)
        r = merge_sort(ary, mid+1, right)
        return merge(l, r) # conquer

    else:
        return [ary[left]]




if __name__ == '__main__':
    a = [6,56,65,6,5,5,251,45,23,2,21]
    b = [6,56,65,6,5,5,251,45,23,2,21]
    print(merge_sort(a, 0, len(a)-1))
    b.sort()
    print(b)
