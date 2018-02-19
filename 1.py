import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a % 1) == 0:
    a = int(a)
if (b % 1) == 0:
    b = int(b)
if (c % 1) == 0:
    c = int(c)
if a == 0 and b == 0:
    print("y = ", c)
    print("x - any")
else:
    if a == 0:
        if c == 0:
            print("y = ", b, "x")
            print("x = ", c)
        else:
            print("y = ", b, "x + ", c)
            print("x = ", -c / b)
    elif b == 0:
        if c == 0:
            print("y = ", a, "x^2")
            print("x = ", c)
        else:
            print("y = ", a, "x^2 + ", c)
            if (a > 0 and c > 0) or (a < 0 and c < 0):
                print("x - complex")
            else:
                print("x1 = ", math.sqrt(-c / a))
                print("x2 = ", -math.sqrt(-c / a))
    else:
        print("y = ", a, "x^2 + ", b, "x + ", c)
        if (b ** 2 - 4 * a * c) < 0:
            print("x - complex")
        elif (b ** 2 - 4 * a * c) == 0:
            print("x = ", -b / 2 / a)
        else:
            print("x1 = ", (-b + math.sqrt(b ** 2 - 4 * a * c) / 2 / a))
            print("x2 = ", (-b - math.sqrt(b ** 2 - 4 * a * c) / 2 / a))
