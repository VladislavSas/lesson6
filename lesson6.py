A = int(input("Введите значение числа А: "))
n = int(input("Введите значения степени n: "))
x = 1
while True:
    xk_1 = (1/n) * ((n-1) * x + A / x**(n-1))
    if xk_1 == x:
        break
    x = xk_1
    print (xk_1)

 