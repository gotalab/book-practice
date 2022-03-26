# 各列に一個の王妃を配置する組み合わせを再帰的に列挙

pos = [0] * 8

def put() -> None:
    """盤面（各列の王妃の位置）を出力"""
    for i in range(8):
        print(f'{pos[i]:2}', end=" ")
    print()

def set(i: int) -> None:
    """i列目に王妃を配置"""
    for j in range(8):
        pos[i] = j
        if i == 7:
            put()
        else:
            set(i+1)

if __name__ == '__main__':
    put()