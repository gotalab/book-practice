# 1000以下の素数を列挙
counter = 0

for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)

print(f'除算を行った回数:{counter}')
