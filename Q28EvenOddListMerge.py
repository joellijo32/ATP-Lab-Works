def seperator(list_1, list_2): 
    odd_list = []
    even_list = []

    iterating_list = list_1 + list_2
    # Seperating Even and Odd
    
    for i in iterating_list :  
        if i%2 == 0: 
            even_list.append(i)
        else: 
            odd_list.append(i)
    # Sorting

    odd_list.sort()
    even_list.sort()

    # Merging

    return even_list + odd_list

list_one = []
list_two = []
limit_of_first_list = int(input("\nEnter the limit of the First List: "))
print("Enter the First List: ")
for i in range(limit_of_first_list): 
    list_one.append(int(input()))

limit_of_second_list = int(input("\nEnter the limit of the Second List: "))
print("Enter the Second List: ")
for i in range(limit_of_second_list): 
    list_two.append(int(input()))

print()
print("Required List Output: ",seperator(list_one,list_two))


