#Kalen Funai
#09/29/2023
#CarBotds

name = input("What is your name?")
print("Hi",name,"! Nice to meet you, I am CarBot!")

location = input("Where are you from?")
print(location,"sounds like a great place, I've always wanted to go there!")

print("I love numbers!")
favNumber = input("What is your favorite number?")
newNumber = 3 + int(favNumber)
print("Your favorite number plus my favorite number is",newNumber,"!")

dreamCar = input("What is your dream car?")
print("Woah a",dreamCar,"that's a cool car, good choice!")
cost = input("What does this car cost?")
interest = input("What is the annual interest rate for a car loan!")
r = float(interest)/100/12
loan = input("If you had to take out a car loan how many years would you take the loan out for?")
n = int(loan) * 12
monthlyPayment = (r * int(cost)) / (1 - (1 + r) ** -n)

print("The monthly payment with interest will be,", round(monthlyPayment, 2))

totalCost = int(monthlyPayment) * (12*int(loan))
print("Your total cost will be", round(totalCost, 2), ",I hope that works for you!")