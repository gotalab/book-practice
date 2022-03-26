# マージソート
from tkinter import N
from typing import MutableSequence
def merge_sort(a: MutableSequence) -> None:
    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left]~a[right]を再帰的にマージソート"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center) # 前半部をマージソート
            _merge_sort(a, center + 1, right) # 後半部をマージソート

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff

if __name__  == '__main__':
    print('マージソート')
    num = int(input('要素数：'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))
    merge_sort(x)
    print('昇順にソートしました')
    for i in range(num):
        print(f'x[{i}]={x[i]}')
