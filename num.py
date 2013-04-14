#coding: utf-8

def is_prime(n):
    flag=True

    if n < 2:
        flag = False

    for i in range(2,n-1):
        if n % i == 0:
            flag = False

    if flag == True:
        return flag

for i in range(0,2000000):
    if is_prime(i):
        print i
