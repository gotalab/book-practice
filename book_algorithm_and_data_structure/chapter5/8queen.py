# 各行、各列に一個の王妃を配置する組み合わせを再帰的に列挙

pos = [0] * 8 # 各列の王妃の位置
flag_a = [False] * 8 # 各行に王妃が配置済みか
flag_b = [False] * 15 # 対角線（/）に王妃が配置済みか
flag_c = [False] * 15 # 対角線（\）に王妃が配置済みか

def put() -> None:
    """盤面（各列の王妃の位置）を出力"""
    for i in range(8):
        print(f'{pos[i]:2}', end=" ")
    print()

def set(i: int) -> None:
    """i列目の適切な位置に王妃を配置"""
    for j in range(8):
        if (not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 7]):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i+1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

if __name__ == '__main__':
    set(0)