import numpy as np


def cal():
    print("Enter 6 coefs, first must be  >  0:")
    #number_array = list()
    number = 6

    while (True):
        number_array = list(map(float, input("").split()))
        if (len(number_array) == 6):
            break
        else:
            print("Wrong input. Please enter 6 ploy5 coefficients: ")
    j = 5
    for i in number_array:
        print("a", j, " = %.3f" % i)
        j = j - 1

    a = np.roots(number_array)
    reversed_arr = a[::-1]

    print("Solutions are: ")
    for i in reversed_arr:
        k = "%.6f + %.6fi" % (i.real, i.imag)
        print(k)


cal()
