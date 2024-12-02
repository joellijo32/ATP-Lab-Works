#Day One 

print("\n")
money_left = int(input("Enter the Amount of Left : "))
percent_to_spend = float(input("Enter the Percentage of Amount Willing to Spend (without \'%\' symbol) : "))
print("Enter the Cost of the Items (3 Nos) Bought : ")
list_of_cost = []
for i in range(3): 
    list_of_cost.append(float(input()))
amount_that_can_be_spent = float((money_left*percent_to_spend)/100)
total_cost = sum(list_of_cost)
if total_cost > amount_that_can_be_spent: 
    print("The Items CANNOT be bought.")
    print("Lack of ",(total_cost-amount_that_can_be_spent)," Amount of Money")
else: 
    print("The Items CAN be bought")
    if (amount_that_can_be_spent-total_cost) > 0 : 
        print("Balance Would be ", (amount_that_can_be_spent-total_cost), " Amount of Money")
    else: 
        print("Balance Amount: " , 0)
print("\n")                
