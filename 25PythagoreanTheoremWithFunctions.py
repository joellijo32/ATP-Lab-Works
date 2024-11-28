a = 0
b = 0
c = 0

def input_lengths(): 
    global a,b,c
    a = int(input("Enter the Three Sides of the Triangle: "))
    b = int(input())
    c = int(input())

def is_right_angled_triangle(): 
    global a,b,c
    if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2):
        return True
    return False 
    

def result(): 
    if is_right_angled_triangle(): 
        print("The Triangle is Right-Angled...!")
    else: 
        print("The Triangle is NOT Right-Angled....")

input_lengths()
result()