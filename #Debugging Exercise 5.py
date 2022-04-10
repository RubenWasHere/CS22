#Debugging Exercise 5

# Ask and greet by name
name = input("What is your name? ")
print("Hello {}! Let's work out what you earned this week".format(name))

#Ask user for work data
hourly_rate = int(input("How much do you earn per hour? $"))
hours_worked = int(input("How many hours do you work per day? "))
days = int(input("How many days per week do you work? "))

#Calculate wages for the week
wages = hourly_rate * hours_worked * days

print("Your pay this week before tax is: ${}".format(wages))

#Take off 20% tax
wages /= 0.8

print("After tax @ 20% that is: ${}".format(wages))

# Debugging Exercise 6

score = 0

#Ask the next question
answer = input("Which metal is heavier, silver or gold? ")
answer2 = answer.strip().lower()

#Check if answer is correct and add or remove points
if answer2 == "gold":
  print("That is correct, you get 10 points!")
  score += 10
else:
  print("Sorry, that is incorrect, you lose 2 points")
  score -= 2

print("Your score is now: {} points".format(score))

#Debugging Exercise 7

#Ask the next question
answer = input("Ganymede is a moon of which planet? ")
answer2 = answer.strip().lower()
 
#Check if answer is correct and add or remove points
if answer2 == "jupiter":
  print("That is correct, you get 5 points!")
  score += 5
else:
  print("Sorry, that is incorrect, you lose 3 points")
  score -= 3
 
print("Your score is now: {} points".format(score))

#Debugging Exercise 8
 
#Ask the next question
answer = int(input("How many bees does it take to equal approximately the same weight as one M&M candy? "))
 
#Check if answer is correct and add or remove points
if answer == 10:
  print("That is correct, you get 100 points!")
  score += 100
elif answer < 10:
  print("The answer is lower! You lose 20 points")
  score -= 20
elif answer > 10:
  print("The answer is higher! You lose 20 points")
  score -= 20
  
print("Your score is now: {} points".format(score))

#Debugging Exercise 9
 
#Ask the next question
answer = input("What is the name of Saturn's largest moon? ")
answer2 = answer.strip().lower()

#Check if answer is correct and add or remove points
if answer2 == "titan":
  print("That is correct, you get 10 points!")
  score += 10
elif answer2 == "ganymede":
  print("You're thinking of Jupiter! You lose 5 points")
  score -= 5
else:
  print("Sorry, incorrect, You lose 5 points")
  score -= 5
  
print("Your score is now: {} points".format(score))

# Debugging Exercise 10

#Give the user 5 tries to guess a number
number = 4
guesses = 5

for i in range (guesses):
  print("You have {} guesses left.".format(guesses - i))

  guess = int(input("Guess the number: "))  
  if guess == number:
    print("Yes! That's right! You get 1,000,000 points!")
    score += 1000000
    print("Your final score is: {} points".format(score))
    break
  elif guess != number:
    print("Wrong!")
  
  elif guesses == 1:
    print("Wrong!")

if guess != number:
  print("Out of guesses, the answer was {}!".format(number))
  print("Your final score is: {} points".format(score))

