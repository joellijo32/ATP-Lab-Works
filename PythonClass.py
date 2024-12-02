from datetime import datetime
print("\n")
date = input("Enter Your Birthdate in the format dd-mm-yyyy : ")
values = date.split("-")
day = int(values[0])
month = int(values[1])
year_of_birth = int(values[2])
year_after_birth = int(datetime.now().year - year_of_birth)

print("You are ", year_after_birth, "Years old.")

end_date = datetime(int(datetime.now().year),int(datetime.now().month),int(datetime.now().day ))
start_date = (datetime(year_of_birth ,month, day))
nnumber_of_days_lived  =  int((end_date - start_date).days)

print("You've Lived " , nnumber_of_days_lived, " Days....bruh")

print("\n")







