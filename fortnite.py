#Ask for age to find out if they are 16 or over (Old enough to apply for learners license)

learner=16

age = int(input("What is your age? "))

if age >= learner:
    print("You can apply for a learners licence!") 


if age < learner:
    print("You are uneligible for a learners licence.")


