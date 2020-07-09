import numpy as np


#print("done")
#number_array = [720, -612, -500, 449, 52, -60]

print("Enter 6 coefs, first must be  >  0:")
#number_array = list()
number = 6
#for i in range(6):
#   n = input("")
#  number_array.append(int(n))
while (True):
    number_array = list(map(float, input("").split()))
    if (len(number_array) == 6):
        break
    else:
        print("Wrong input. Please enter 6 ploy5 coefficients: ")

print("a5 = ", number_array[0])
print("a4 = ", number_array[1])
print("a3 = ", number_array[2])
print("a2 = ", number_array[3])
print("a1 = ", number_array[4])
print("a0 = ", number_array[5])

p = np.poly1d(number_array)

k = 0
while (p(2**k) <= 0):
    k = k + 1

high = 2**k
#print("high = ", high)


k = 0
while (p((2 ** k)*(-1)) >= 0):
    k = k + 1

low = (2 ** k)*(-1)
#print("low = ", low)


while((high - low) >= 0.0000000001):
    mid = (high+low)/2
    if(p(mid)*p(low) < 0):
        high = mid
    else:
        low = mid

#print("low = ", low, "high = ", high)
print("ploy5(", round(low, 6), ") = ", 0.000000)
print(" ")
print("Hence one real root is: x* = ", round(low, 6))




