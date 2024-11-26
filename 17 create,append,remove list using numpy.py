import numpy as np
print("Enter the size of the List: ",end="")
size = int(input())
print(f"Enter {size} elements: ")
list_of_elements =np.array([], dtype=int)
for i in range(size): 
    value = int(input())
    list_of_elements = np.append(list_of_elements, int(value))
    
print("The List Entered: ")
print( np.array2string(list_of_elements,separator=", "))



print("Enter the numbers of elements to be appended: ",end="")
size_of_elements_to_append  = int(input())
if size_of_elements_to_append > 0 :
    print("Enter the Elements to be appended: ")
    for i in range(size_of_elements_to_append): 
        value = int(input())
        list_of_elements = np.append(list_of_elements,value)

    print("Appended List: ")
    print(np.array2string(list_of_elements,separator=", "))

print("Enter the number of elements to be Removed: ",end="")
number_of_elements_to_remove = int(input())
if number_of_elements_to_remove > 0 : 
    print("Enter the Elements to remove: ")
    for i in range(number_of_elements_to_remove):
        value = int(input())
        index = np.where(list_of_elements == value)
        list_of_elements = np.delete(list_of_elements,index)
        print("Removed :",value)

    print("List after removing elements: ")
    print(np.array2string(list_of_elements,separator=", "))