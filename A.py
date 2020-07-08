import numpy as np

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
#print("done")

print("a5 = ", number_array[0])
print("a4 = ", number_array[1])
print("a3 = ", number_array[2])
print("a2 = ", number_array[3])
print("a1 = ", number_array[4])
print("a0 = ", number_array[5])

low = -1000000000
high = 100000000000
p = np.poly1d(number_array)

while((high-low) >= 0.000000000000001):

    #print("inside")
    mid = (high+low)/2
    if(p(mid) == 0):
        print(mid)
        break
    elif(p(mid)*p(low) < 0):
        high = mid
    else:
        low = mid

print("ploy5(", round(low, 6), ") = ", 0.000000)
print(" ")
print("Hence one real root is: x* = ", round(low, 6))




