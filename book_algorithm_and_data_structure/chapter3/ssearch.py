# 線形探索
from typing import Any, Sequence

def seq_search_while(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと透過な要素を線形探索"""
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

def seq_search_for(a: Sequence, key: Any) -> int:
    """シーケンスaからkeyと透過な要素を線形探索"""
    for i in range(len(a)):
        if a[i] == key:
            print(i)
            return i
    return -1

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    ky = int(input('探す値：')) #キーkyの読み込み

    idx = seq_search_for(x, ky)

    if idx == -1:
        print('その値の要素は存在しません')
    else:
        print(f'それはx[{idx}]にあります')