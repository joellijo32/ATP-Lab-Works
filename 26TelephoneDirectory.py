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
        print("\n\nEnter the Name of the Contact: ",end="")
        name = input()
        print("Enter the Number: ",end="")
        number = int(input())
        telephone_directory[name] = number
        print("\nThe Contact has been Successfully Added.")
    
    # Updating 

    elif choice == 2: 
        print("\n\nEnter the Name of the Contact to Udate: ",end="")
        name = input()
        if name not in telephone_directory: 
            print(f"{name} is Not in the Directory. Updation Failed .")
            continue
        else: 
            print("Enter the Number to Update: ",end="")
            number = int(input())
            telephone_directory.update({name : number})
            print("\nThe Number has been Updated Successfully.")
    
    # Deleting

    elif choice == 3 : 
        name = input("\n\nEnter the Name of the Contact to Delete: ")
        if name not in telephone_directory: 
            print(f"{name} Not Found in the Directory. Deletion Failed.")
        else: 
            telephone_directory.pop(name)
            print("The Contact has been Deleted Successfully.")
    
    # Searching

    elif choice == 4: 
        name = input("\n\nEnter the Name to Search: ")
        if name not in telephone_directory : 
            print(f"{name} Not Found in the Directory.")
        else: 
            print("Contact Found : ")
            print(name , ":", telephone_directory[name])
    
    # Displaying

    elif choice == 5: 
        print("\n\nDisplaying All the Contacts: \n")
        for i in telephone_directory: 
            print(i,":",telephone_directory[i])
        print("\nEnd of the List.")

    # Exit 

    elif choice == 6: 
        print("\n\nExiting the Program.\n")
        break



    
