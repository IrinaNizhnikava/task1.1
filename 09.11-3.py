def degree(x):
    spis = [x * x * x for _ in range(1)]
    print(spis[0])
if __name__:
    i = int(input("введите число "))
    degree(i)