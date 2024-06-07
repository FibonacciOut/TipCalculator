
print("How much is the bill?")
amount = input()
print("How many people are spliting the bill?")
peeps = input()
total = float(amount)
people = float(peeps)
amount = total/people
amount = str(amount)
print("Each person will pay " + amount + " Dollars")
#Tipping
# y = "yes"
# n = "no"
print("Would you like to tip? y/n")
going_to_tip = input()
if going_to_tip == "yes"[0]:
    print("What percent would you like to tip?")
    tip_Percent = input()
    tip_Percent = float(tip_Percent)
    tip_amount = tip_Percent / 100
    amount = float(amount)
    tip_amount = tip_amount * amount
    tip_amount = str(tip_amount)
    print("The tip amount will be " + tip_amount + " Dollars")
if going_to_tip == "no"[0]:
    print("Dang, Okay the service must have sucked.")

#Need to make if statment registar just first letter 
#formula for getting the tip amount
# thats how you split a bill  Amount divided by the number of people 