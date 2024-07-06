import matplotlib.pyplot as plt
import numpy as np
from prime import primelist

# x = [1,2,3,4,5]
# y = [1,2,3,4,5]
# plt.plot(x,y)
# plt.show()

# user_inp1 = input("Enter your data separated by spaces: ").split()
user_inp1 = input("Input a number for all the primes that come before it: ")
# user_inp2 = input("Enter the title for the x-axis: ")
# user_inp3 = input("Enter the title for the y-axis: ")
# arr = [int(num) for num in user_inp1]
arr = primelist(int(user_inp1))
# print(arr)
n = len(arr)
x = [int(num+1) for num in range(n)]

sumOfProd = 0
sumOfX = sum(x)
sumOfY = sum(arr)
sumOfSqrX = 0
sumOfXSqr = sumOfX*sumOfX
aveY = sumOfY/n
aveX = sumOfX/n
for i in range(n):
    sumOfProd = sumOfProd+ x[i]*arr[i]
for i in range(n):
    sumOfSqrX = sumOfSqrX + (x[i]*x[i])
a1 = (n*sumOfProd - (sumOfX*sumOfY))/((n*sumOfSqrX)-sumOfXSqr)
a0 = aveY - (a1*aveX)

def f(xval):
    return a0 + a1*xval
xval = np.linspace(0, n+1, 10000)
y = f(xval)



print(arr)
plt.scatter(x,arr)
plt.plot(xval,y)
plt.title('All the prime numbers up to ' + user_inp1)
plt.xlabel('Index')
plt.ylabel('Prime Numbers')

#
# for i, txt in enumerate(zip(x, arr)):
#     plt.annotate(txt, (x[i], arr[i]), textcoords="offset points", xytext=(0,5), ha='center')


plt.show()
