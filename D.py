import numpy as np


def cal():
    print("Enter 7 coefs, first must be  >  0:")
    #number_array = list()
    number = 7
    while (True):
        number_array = list(map(float, input("").split()))
        if (len(number_array) == 7):
            break
        else:
            print("Wrong input. Please enter 6 ploy5 coefficients: ")
    #for i in range(int(number)):
    #   n = input("")
    #   number_array.append(int(n))
    j = 6
    for i in number_array:
        print("org", j, " = %.3f" % i)
        j = j - 1

    # j=5
    # for i in number_array:
    #     print("derived coeff")
    #     j=j-1

    new_array = list()

    new_array.append(number_array[0] * 6)
    new_array.append(number_array[1] * 5)
    new_array.append(number_array[2] * 4)
    new_array.append(number_array[3] * 3)
    new_array.append(number_array[4] * 2)
    new_array.append(number_array[5])
    a = np.roots(new_array)
    for i in a:
        print(i)
    reversed_arr = a[::-1]
    real = list()
    print("Solutions are: ")
    for i in reversed_arr:
        k = "%.6f + %.6fi" % (i.real, i.imag)
        print(k)
        t = "%.6f " % (i.real)
        real.append(t)
    print(" ")
    p = np.poly1d(number_array)
    minival = 100000000000000000000000000000000000000000
    #print(p(a[0].real))

    for i in a:
        print("p6(", round(i.real, 6), ") =", end=" ")
        x = p(round(i.real, 6))
        x = round(x, 6)
        print(x)
        minival = min(minival, x)

    print(" ")
    print("Analyzing real roots of the derivative:")
    print(" ")
    print("Global Minimum value =", end=" ")
    print(minival)
    print(" ")
    print("Global Minimum Point:")
    for i in a:
       x = p(round(i.real, 6))
       x = round(x, 6)
       if (x == minival):
           print("x* =", end=" ")
           print(round(i.real, 6))


cal()
