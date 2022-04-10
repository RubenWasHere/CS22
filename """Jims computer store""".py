"""Jims computer store""" 
"""Allow users to be able to purchase a small range of computers from "Jims Computer Store"""
"""Date: 18nd June 2021"""
"""Wrriten by: Ruben Bharot"""

#Create banner
def banner():
    print("////////////////////////////////////")
    print("/////// Jims Computer Store ////////")
    print("////////////////////////////////////")

#Call banner function
banner()

#Create list of computer options for purhcase
computer_list = ["Home Basic - $1000 - 4GB RAM - Built in Graphics - 50cm Monitor", "Office - $1500 - 8GB RAM - Built in Graphics - 60cm Monitor", "Gamer - $2000 - 16GB RAM - 4GB Nvidia Graphics - 70cm Monitor", "Studio - $2500 - 16GB RAM - 4GB Nvidia Graphics - Dual 60cm Monitor"]

#Print list of computer options for purhcase
count = 0
while count < 4:
    print(computer_list[count])
    print()
    count = count + 1

#Ask user for name letters only
while True:
        name = input("What is your first name? (Use only letters): ")
        print()
        if name.isalpha():
            break
name = str(name)

#Ask for age 
while True:
        age = input("What is your age? (Use only numbers): ")
        print()
        if age.isnumeric():
            break
age = int(age)

#Ask for amount of money for a desposit
while True:
        deposit =(input("How much money do you have for a deposit? (Use only numbers) $"))
        print()
        if deposit.isnumeric():
            break
deposit = int(deposit)

#Ask for cost of the computer they want to purchase
while True:
        computer_cost =(input("How much does the computer you want cost? (Use only numbers) $"))
        print()
        if computer_cost.isnumeric():
            break
computer_cost = int(computer_cost)

#If age <= 21 and if they don't have enough say they can save and then come in store and print banner
    #If age <= 21 and if they do have enough ask to confirm purchase and print receipt and banner if they say yes and purchase cancelled and banner printed if no 
if age < 21:
    if deposit >= computer_cost:
        print(name, "you have $", deposit, "and the computer you want costs $", computer_cost, "so you can buy the computer of your choice")
        print()

        while True:
            confirmation = input("Please confirm that you would like to make this purchase (Yes or No): ")
            print()
            if confirmation == "Yes":
                print(name, "successfully purchased computer for", computer_cost)
                print()
                banner()
                break
            elif confirmation == "No":
                print("Purchase cancelled, Goodbye.")
                print()
                banner()
                break
    else:
        print ("You do not have enough money to make this purchase, please keep saving and come in store.") 
        print()
        banner()

#If age >= 21 and they have enough then ask to confirm purchase and print receipt and banner if they say yes and purchase cancelled and banner printed if no
#If age >= 21 and they don't have enough say that they can apply for a hire purchase with a deposit of deposit + $50 administration fee and either 12 or 24 m#onths confirm whether they would like to do this, if yes then ask either 12 or 24 months and print their receipt if not print message banner
if age >= 21:
    if deposit >= computer_cost:
        print(name, "you have $", deposit, "and the computer you want costs $", computer_cost, "so you can buy the computer of your choice")
        print()

        while True:
            confirmation = input("Please confirm that you would like to make this purchase (Yes or No): ")
            print()
            if confirmation == "Yes":
                print(name, "you have successfully purchased computer for", computer_cost)
                print()
                banner()
                break
            elif confirmation == "No":
                print("Purchase cancelled, Goodbye.")
                print()
                banner()
                exit()
                
    if deposit <= computer_cost:
        print(name, "you have", deposit, "and the computer you want costs", computer_cost, "sadly you are short by $", computer_cost - deposit, "but you can make a hire purchase for the computer with a $50 Administration Fee that needs to be paid as part of the intial cost.")
        hire_purchase = deposit + 50
        print()
        print("Your deposit will be $", deposit + 50, "which includes the $50 Administration Fees")
        print()
        print("There are two options for hire purchase - 12 months or 24 months.")
        print()

        while True:
            hire_purchase_conformation = input("Please confirm if you would like to purchase the computer using a hire purchase (Yes or No): ")
            print()
            if hire_purchase_conformation == "Yes":
                break
            elif hire_purchase_conformation == "No":
                print("Purchase cancelled, Goodbye.")
                print()
                banner()
                exit()
            
    if hire_purchase_conformation == "Yes":
        while True:
            months = input("Which hire purchase option would you like to go for? (12 months or 24 months): ")
            print()
            if months == "12":
                print(name, "successfly hire purchased for", months, "months with deposit of $", hire_purchase)
                banner()
                break
            elif months == "24":
                print(name, "successfly made a hire purchase for", months, "months with deposit of $", hire_purchase)
                banner()
                break
            
    if hire_purchase_conformation == "No":
        print("Purchase cancelled, Goodbye.")
        print()
        banner()
        exit()        