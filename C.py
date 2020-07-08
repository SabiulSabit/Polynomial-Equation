import numpy as np

def cal():
    print("Enter 6 coefs, first must be  >  0:")
    number_array = list()
    number =6
    for i in range(int(number)):
        n = input("")
        number_array.append(int(n))
    j=5        
    for i in number_array:
        print("a",j," = %.3f"%i)
        j=j-1
        
    a = np.roots(number_array)
    reversed_arr = a[::-1]

    print("Solutions are: ")
    for i in reversed_arr:
        k = "%.6f + %.6fi"%( i.real,i.imag)
        print(k)
        
cal()