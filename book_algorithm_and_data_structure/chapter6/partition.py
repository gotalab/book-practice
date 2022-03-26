# 配列の分割
from typing import MutableSequence

def partition(a: MutableSequence) -> None:
    """配列を分割して表示"""
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'枢軸の値は{x}です')
    print(f'枢軸以下のグループ')
    print(*a[0:pl])

    if pl > pr + 1:
        print('枢軸と一致するグループ')
        print(*a[pr + 1:pl])

    print(f'枢軸以上のグループ')
    print(*a[pr + 1:n])

if __name__  == '__main__':
    print('配列の分割')
    num = int(input('要素数：'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))
    partition(x)
    # print('昇順にソートしました')
    # for i in range(num):
    #     print(f'x[{i}]={x[i]}')