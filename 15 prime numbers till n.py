from math import *
n = int(input("N = "))
counter = 0
for i in range(2,n): 
    is_prime = True
    for j in range(2,int(sqrt(i))+1):  
        if i % j == 0: 
            is_prime = False
            break
    if is_prime:
        if counter == 0: 
            print(i)
            counter = 1
        else: 
            counter = 0
