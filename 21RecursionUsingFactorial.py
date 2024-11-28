def factorial(fact): 
    if fact == 0: 
        return 1
    else: 
        return fact * factorial(fact-1)
    
print("Enter a Number: ",end="")
number = int(input())
factorial_of_number = factorial(number)
print(f"Factorial of {number} = {factorial_of_number}")
