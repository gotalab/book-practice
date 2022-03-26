from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート（第二版：交換回数による打切り）"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0 # パスにおける交換回数
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1

        if exchng == 0:
            break