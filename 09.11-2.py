def minn(a, b, c):
    if a < b:
        if a < c:
            print(a, " наименьшее число")
        elif a > c:
            print(c, " наименьшее число")
        else:
            print(a, " равно ", c)
    elif a > b:
        if b < c:
            print(b, " наименьшее число")
        elif b > c:
            print(c, " наименьшее число")
        else:
            print(b, " равно ", c)
    elif a == b:
        if a > c:
            print(c, " наименьшее число")
        elif a < c:
            print(a, " равно ", b, " и меньше ", c)
        else:
            print("числа равны")

if __name__:
    spis = [input("Введите число: ") for _ in range(3)]
    minn(spis[0], spis[1], spis[2])