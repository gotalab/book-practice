from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    """単純交換ソート（第二版：交換回数による打切り）"""
    n = len(a)
    k = 0

    while k < n - 1:
        last = n - 1
        for i in range(n - 1, k, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                last = i
        k = last