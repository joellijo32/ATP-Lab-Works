telephone_directory = {}

while True: 
    
    print("\nEnter 1 to Add a Contact")
    print("\nEnter 2 to Update a Contact")
    print("\nEnter 3 to Delete a Contact")
    print("\nEnter 4 to Search for a Contact")
    print("\nEnter 5 to Display All the Contacts")
    print("\nEnter 6 to Exit")
    print("\nEnter the Choice: ",end="")
    choice = int(input())

    # Adding

    if choice == 1: 
        print("\nEnter the Name of the Contact: ",end="")
        name = input()
        print("\nEnter the Number: ",end="")
        number = int(input())
        telephone_directory[name] = number
        print("\nThe Contact has been Succesfully Added.")
    
    # Updating 

    elif choice == 2: 
        print("\nEnter the Name of the Contact to Udate: ",end="")
        name = input()
        if name not in telephone_directory: 
            print(f"{name} is Not in the Directory")
            continue
        else: 
            print("Enter the Number to Update: ",end="")
            number = int(input())
            telephone_directory.update({name : number})
            print("\nThe Number has been Updated Succesfully.")
    
    # Deleting

    pass
