def max3(a, b, c):
    """a, b, cの最大値を求めて返却"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum
