telephone_directory = {}

while True: 
    print("\nTelephone Directory Menu: ")
    print("1. Add a Contact")
    print("2. Update a Contact")
    print("3. Delete a Contact")
    print("4. Search for a Contact")
    print("5. Display all the Contacts")
    print("6. Exit")
    print("Enter the Choice (1-6): ",end="")
    choice = int(input())

    # Adding

    if choice == 1: 
        print("Enter the Name of the Contact: ",end="")
        name = input()
        print("Enter the Number: ",end="")
        number = int(input())
        telephone_directory[name] = number
        print("The Contact has been Successfully Added.")
    
    # Updating 

    elif choice == 2: 
        print("Enter the Name of the Contact to Udate: ",end="")
        name = input()
        if name not in telephone_directory: 
            print(f"{name} is Not in the Directory. Updation Failed .")
            continue
        else: 
            print("Enter the Number to Update: ",end="")
            number = int(input())
            telephone_directory.update({name : number})
            print("The Number has been Updated Successfully.")
    
    # Deleting

    elif choice == 3 : 
        name = input("Enter the Name of the Contact to Delete: ")
        if name not in telephone_directory: 
            print(f"{name} Not Found in the Directory. Deletion Failed.")
        else: 
            telephone_directory.pop(name)
            print("The Contact has been Deleted Successfully.")
    
    # Searching

    elif choice == 4: 
        name = input("Enter the Name to Search: ")
        if name not in telephone_directory : 
            print(f"{name} Not Found in the Directory.")
        else: 
            print("Contact Found : ")
            print(name , ":", telephone_directory[name])
    
    # Displaying

    elif choice == 5: 
        print("Displaying All the Contacts: \n")
        for i in telephone_directory: 
            print(i,":",telephone_directory[i])
        print("End of the List.")

    # Exit 

    elif choice == 6: 
        print("Exiting the Program.\n")
        break



    
