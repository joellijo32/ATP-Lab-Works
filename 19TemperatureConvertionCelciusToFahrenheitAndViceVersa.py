print("\nTemperature Conversion")
print("\nEnter From Temperature: (c) for Celsius & (f) for Fahrenheit: ",end="")
from_degree = input()
if from_degree == "c": 
    print("Enter the Temperature in Degree Celcius: ",end="")
    degree_celcius = float(input())
    degree_fahrenheit = float(((9*degree_celcius)/5) + 32)
    print(f"{degree_celcius} deg Celcius = {degree_celcius} deg Fahrenheit")
elif from_degree == "f" : 
    print("Enter the Temperature in Degree Fahrenheit: ",end="")
    degree_fahrenheit = float(input())
    degree_celcius = float(((degree_fahrenheit-32)/9)*5)
    print(f"{degree_fahrenheit} deg Fahrenheit = {degree_celcius} deg Celcius ")

print("\n")

