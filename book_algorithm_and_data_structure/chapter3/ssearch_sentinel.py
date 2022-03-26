# 線形探索（番兵法）
from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq) # seqのコピー
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('要素数：'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]：'))

    ky = int(input('探す値：')) #キーkyの読み込み

    idx = seq_search(x, ky)

    if idx == -1:
        print('その値の要素は存在しません')
    else:
        print(f'それはx[{idx}]にあります')