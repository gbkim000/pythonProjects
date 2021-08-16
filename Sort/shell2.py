from typing import MutableSequence
from random import *


def shell_sort2(a: MutableSequence) -> None:
    n = len(a)
    h = 1
    while h < n // 9:  # (h갑을 h*3+1 수열을 사용하면 효율적 가능.)
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            temp = a[i]
            while j >= 0 and a[j] > temp:
                a[j + h] = a[j]
                j = j - h
            a[j + h] = temp
        h = h // 3


if __name__ == '__main__':

    # num = int(input(('정렬할 자료 갯수: ')))
    num = 100
    x = [None] * num

    print('쉘 정렬을 수행합니다.')
    for i in range(num):
        # x[i] = int(input(f'x[{i}:] '))
        x[i] = randint(1, 100)
        print(f'{x[i]:4}', end='')

    shell_sort2(x)
    print()
    print('-' * 4 * num)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')
