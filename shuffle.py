import random


def shuffle(a):
    for i in range(len(a)):
        r = random.randint(i, len(a)-1)
        a[i], a[r] = a[r], a[i]
    return a

if __name__ == '__main__':
    a = [x for x in range(10)]

    for i in range(len(a)):
        r = random.randint(i, len(a)-1)
        a[i], a[r] = a[r], a[i]

    print(a)
