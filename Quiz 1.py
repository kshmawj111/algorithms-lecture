def check_sorted_in_ascending(a: list):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False

    return True

if __name__ == '__main__':
    a = [1, 2, 3, 2, 5]
    print(check_sorted_in_ascending(a))