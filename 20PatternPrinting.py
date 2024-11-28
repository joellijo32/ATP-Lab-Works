 #a
print("\n")
for i in range(6): 
    for j in range(i+1):
        print("*",end=" ")
    print("\n")


#b
print("\n\n")
starting_point = 6
for i in range(6): 
    for j in range(11):
        if j == starting_point : 
            print("* "*(i+1))
            starting_point = starting_point - 1
        print(" ",end="")
    print("\n")


#c 

print("\n\n")
counter = 0
starting_point = 6
for i in range(7): 
    if i > 3 : 
        if counter == 0: 
            starting_point += 1
            counter += 1
        starting_point += 1
    for j in range(11): 
        if i <=3 : 
            if j == starting_point: 
                print("* "*(i+1))
                starting_point -= 1
            print(end=" ")
                
        else:
            if j == starting_point : 
                print("* "*(7-i))
            print(" ",end="")

    
    
    print("\n")