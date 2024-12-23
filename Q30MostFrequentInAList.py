array = eval(input("Enter the Array: "))


max_count = 0
most_frequent = None


for i in array:
    count = 0
    for j in array:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        most_frequent = i


print(f"The most frequent element is {most_frequent}, which appears {max_count} times.")