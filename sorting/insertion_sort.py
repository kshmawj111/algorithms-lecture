def insert_sort(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x[i]
        while x[j] > key and j >= 0:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = key
    return x


def insert_sort_optimized(x):
    for i in range(1, len(x)):
        j = i - 1
        key = x.pop(i)
        # 메모리 접근 최소화 한 삽입정렬
        while x[j] > key and j >= 0:
            j = j - 1
        x.insert(j+1, key)
    return x


if __name__ == '__main__':
    a = [5,4,3,2,1]
    insert_sort_optimized(a)
    print(a)