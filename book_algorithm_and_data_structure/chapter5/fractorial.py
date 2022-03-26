# 非負の整数の階乗値を求める
# math.fractorial関数が存在するため、別に自作すうｒ必要はない

def fractorial(n: int) -> int:
    if n > 0:
        return n * fractorial(n-1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('何の階乗：'))
    print(f'{n}の階乗は{fractorial(n)}です。')