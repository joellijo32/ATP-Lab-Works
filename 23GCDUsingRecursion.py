def gcd(num_1,num_2): 
    if num_1 == 0  : 
        return num_2
    elif num_2 == 0 : 
        return num_1
    else: 
        return gcd(num_2,num_1%num_2)

number_one = int(input("Enter 2 numbers: "))
number_two = int(input())
print("GCD of the Two Numbers =",gcd(number_one,number_two))