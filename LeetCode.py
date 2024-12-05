telphone_directory = {"Joel" : 8590453367,"Joshu" : 8281426957}
def delete_contact(): 
    print("\nEnter the Name of the Contact to Delete: ",end="")
    name = input()
    print(telphone_directory.pop(name,f"{name} Not Found in the Directory."))
    print(telphone_directory)
delete_contact()