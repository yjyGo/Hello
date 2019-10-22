def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return f(n-1)+f(n-2)


if __name__ == '__main__':
    n = 25
    print(f(n))