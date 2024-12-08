print("\n\t\t\tELECTRICITY BILL CALCULATOR\n")

print("Enter the Number of Each of the Components: \n")


fans = int(input("Number of Fans = "))
if fans < 0: 
    print("INVALID INPUT .")
    exit()

lights = int(input("Number of Lights = "))
if lights < 0: 
    print("INVALID INPUT .")
    exit()

washing_machines = int(input("Number of Washing Machines = "))
if washing_machines < 0: 
    print("INVALID INPUT .")
    exit()

computers = int(input("Number of Computers = "))
if computers < 0: 
    print("INVALID INPUT .")
    exit()

number_of_days = 60  # Two Months With each having 30 Days

charge_for_fan = 3000*fans
charge_for_light = 1500*lights
charge_for_washing_machines = 6000*washing_machines
charge_for_computers = 9000*computers

print("\n\nCharge for Fans = ₹" + str(charge_for_fan))
print("\nCharge for Lights = ₹" + str(charge_for_light))
print("\nCharge for Washing Machines = ₹" + str(charge_for_washing_machines))
print("\nCharge for Computers = ₹" + str(charge_for_computers))

total_amount = charge_for_computers + charge_for_fan + charge_for_light+charge_for_washing_machines

print("\n\nTotal Amout = ₹" + str(total_amount))
print("\n\n\t\t\tTHANK YOU\n")
