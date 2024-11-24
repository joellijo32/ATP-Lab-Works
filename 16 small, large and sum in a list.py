print("Enter the limit (n) : ")
limit = int(input())

print("Enter",limit,"elements: ")
list_of_n_numbers = []

for i in range(0,limit): 
    list_of_n_numbers.append(int(input()))

maximum = 0
minimum = list_of_n_numbers[0]
sum = 0

for i in list_of_n_numbers: 
    if i > maximum : 
        maximum = i
    if i < minimum : 
        minimum = i
    sum += i
    
print("\nLargest Number in the List =",maximum)
print("\nSmallest Number in the List =",minimum)
print("\nSum of all Elements =",sum)