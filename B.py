import numpy as np

print("Enter 6 ploy5 coefficients:")
number = 6
#for i in range(6):
#n = input("")
#x.append(int(n))
while (True):
    arr = list(map(float, input("").split()))
    if(len(arr) == 6):
        break
    else:
        print("Wrong input. Please enter 6 ploy5 coefficients: ")

print("Enter solution:")
a = float(input(""))

one = arr[0]
two = arr[1]
three = arr[2]
four = arr[3]
five = arr[4]
six = arr[5]


#j = 5
#for i in x:
print("a5 = ", end=" ")
print('%.3f' % one)
print("a4 = ", end=" ")
print('%.3f' % two)
print("a3 = ", end=" ")
print('%.3f' % three)
print("a2 = ", end=" ")
print('%.3f' % four)
print("a1 = ", end=" ")
print('%.3f' % five)
print("a0 = ", end=" ")
print('%.3f' % six)

#j = j - 1


print("xstar =", end=" ")
print(round(a, 6))
a = a * (-1)
x = np.array([one, two, three, four, five, six])
#print(x)
y = np.array([1.0, a])
ans, d = np.polydiv(x, y)
tt = 4
for i in ans:
    print("b",  end="")
    print(tt, " =", end=" ")
    print(round(i, 3))
#print(ans)
