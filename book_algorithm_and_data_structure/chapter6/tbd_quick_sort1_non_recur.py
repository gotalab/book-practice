# クイックソート（非再帰的にも出来る）
# スタックを使用して、スタックに要素のタプルを入れたり出したりしながら並び替える。

from stack import Stack # これは自分で作る必要がある
from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] - a[right]をクイックソート（非再帰）"""
    range = Stack(right - left + 1)
    print(range)


qsort([0, 1, 2, 3, 4, 5, 6, 7], 0, 8)


# if __name__  == '__main__':
#     print('クイックソート（非再帰）')
#     num = int(input('要素数：'))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]：'))
#     quick_sort(x)
#     print('昇順にソートしました')
#     for i in range(num):
#         print(f'x[{i}]={x[i]}')