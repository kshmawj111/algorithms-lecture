def selection_sort(_list: list):
    n_compare = 0
    n_exchange = 0

    for x in range(len(_list)):
        min_i = x

        # 정렬 안된 우측 범위에서 제일 큰 값 하나 고름
        for y in range(x+1, len(_list)):
            n_compare += 1
            # desceding일 땐 부등호 반대로
            if _list[y] < _list[min_i]:
                min_i = y

        n_exchange += 1
        # 값을 swap
        _list[x], _list[min_i] = _list[min_i], _list[x]

    return n_compare, n_exchange


if __name__ == '__main__':
    a = [5,4,3,2,1]
    c, e = selection_sort(a)
    print(a)
    print(f'exchanges: {e}, compares: {c}')