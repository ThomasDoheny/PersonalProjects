import math
def primelist(inp):
    prime_list = []
    for num in range(2, inp+1):
        prime = True
        for i in range(2, int(math.isqrt(num))+1):
            if num%i == 0:
                prime = False
        if prime:
            prime_list.append(num)
    return prime_list

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr


def sort(arr):
    size = len(arr)
    j = size-1
    while j>0:
        for i in range(j):
            if arr[i] > arr[j]:
                swap(arr, i, j)
        j = j-1
    return arr






# user_number = int(input("Please enter an integer: "))
# print(sort(primelist(user_number)))
