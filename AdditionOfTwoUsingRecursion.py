def Add(num_1,num_2): 
    if num_2 == 0: 
        return num_1
    else: 
        return Add(num_1+1 , num_2-1)
    
number_1 = int(input("Enter 2 Numbers: "))    
number_2 = int(input())
print("Sum of the Two Numbers =",Add(number_1,number_2))
