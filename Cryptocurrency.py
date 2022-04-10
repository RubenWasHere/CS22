"""Cryptocurrency""" """Practice assessment task"""
"""Allow users to be able to purchase coins in crypto currency"""
"""Date: 2nd June 2021"""
"""Wrriten by: Ruben Bharot"""

#Create banner and call function

def banner():
    print("////////////////////////////////////")
    print("/// Welcome to the Crypto Market ///")
    print("////////////////////////////////////")

banner()

#Set eligiblity to yes intially
eligble = "yes"

#Ask for name

while True:
        name = input("What is your first name? (Use only letters): ")
        if name.isalpha():
            break
name = str(name)

#Ask for age 
while True:
        age = input("What is your age? (Use only numbers): ")
        if age.isnumeric():
            break
age = int(age)

#If age < 21 ineligible
if age < 21:
    print ("You are too young to be eligible for this program.") 
    eligble = "no"
    banner()
    exit()

#Ask for amount of money 
if eligble == "yes":  
    while True:
        money =(input("How much money do you have? (Use only numbers) $"))
        if money.isnumeric():
            break
money = int(money)

# Print a list of the coins and their prices
coin_list = ["Cardano - $17500.00", "Binance - $6630.00", "Ripple - $15600.00", "Dogecoin - $9999.00", "Tron - $1427.00"]

count = 0
while count < 5:
    print(coin_list[count])
    count = count + 1

coin_purchase = float(input("How much is the coin you would like to purchase? $"))
# money = input("Do you have enough money to purchase that coin? ")

# Work out if they can purchase the coin of their choice

if money >= coin_purchase:
        print(name, "you have", money, "and the coin you want costs", coin_purchase, "so you can buy the coin")
else:
    print(name, "you have", money, "and the coin you want costs", coin_purchase, "sadly you are short on money but you can apply for an interest free loan which can be repayable in 6 months")
    loan = coin_purchase - money
    admin_fee = 100
    total_loan = loan + admin_fee
    monthly_repayments = total_loan / 6
    monthly_repayments = str(round(monthly_repayments, 2))
    print("$",monthly_repayments, "Is your total amount that you must pay every month.")
     




"""Print dict of coins
coindict = {"Cardano $17500.00" : int(17500), "Binance $6630.00" : int(6630), "Ripple $15600" : int(15600), "Dogecoin $9999.00" : int(9999), "Tron $1427.00" : int(1427)}

for value in coindict.items():
    if value <= money:
        condict = {y:x for x,y in coindict.items()}
        print (value)

"""













