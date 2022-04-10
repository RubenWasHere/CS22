#Convert the 0 into a number so we can add scores
score = 0
score = int(score)

#Question1
print("""What is life?
A. No Clue 
B. Beats me...
C. What?
D. 42""")

answer1 = "D"
response1 = input("Your answer is: ")

if (response1 != answer1):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response1 + " is correct!")
    score = score + 1

#Question2
print("""What is 2+2?
A. 5 
B. 4
C. 3
D. 2""")

answer2 = "B"
response2 = input("Your answer is: ")

if (response2 != answer2):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response2 + " is correct!")
    score = score + 1


#Question3
print("""Who has more fortnite wins?
A. Tyler Ninja Blevins
B. Ali-a
C. Some homeless guy
D. Your grandma""")

answer3 = "A"
response3 = input("Your answer is: ")

if (response3 != answer3):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response3 + " is correct!")
    score = score + 1


#Question4
print("""What color ryhmes with door hinge?
A. Black
B. Blue
C. Red
D. Orange""")

answer4 = "D"
response4 = input("Your answer is: ")

if (response4 != answer4):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response4 + " is correct!")
    score = score + 1


#Question5
print("""True or False, Do you exist?
A. Yes
B. No""")

answer5 = "A"
response5 = input("Your answer is: ")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("Well done! " + response5 + " is correct!")
    score = score + 1

print("Your score is " + str(score) + " out of 5")

if score == 5:
    print("Perfect score!")

if score < 5:
    print("Better luck next time!")

if score == 0:
    print("0? Wow.")

if score == 1:
    print("...1? Im sure you can do better than that.")

