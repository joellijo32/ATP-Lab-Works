import numpy as np
print("Enter the size of the List: ",end="")
size = int(input())
print(f"Enter {size} elements: ")
list_of_elements =np.array([])
for i in range(size): 
    value = int(input())
    list_of_elements = np.append(list_of_elements, value)
    
print("The List Entered: ")
print(list(list_of_elements))



print("Enter the numbers of elements to be appended: ",end="")
size_of_elements_to_append  = int(input())
print("Enter the Elements to be appended: ")
for i in range(size_of_elements_to_append): 
    value = int(input())
    list_of_elements = np.append(list_of_elements,value)

print("Appended List: ")
print(list(list_of_elements))

print("Enter the number of elements to be Removed: ")
number_of_elements_to_remove = int(input())
print("Enter the Elements to remove: ")
for i in range(number_of_elements_to_remove):
    value = int(input())
    index = np.where(list_of_elements == value)
    list_of_elements = np.delete(list_of_elements,index)
    print("Removed :",value)

print("List after removing elements: ")
print(list(list_of_elements))
