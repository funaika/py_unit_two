userInput = input("insert number")
number = float(userInput)

print("number of hundreds")
numberOfHundreds = number // 100
print(numberOfHundreds)


changeHundred = number % 100

print("number of tens")
numberOfTens = changeHundred // 10
print(numberOfTens)

changeTen = changeHundred % 10

print("number of ones")
numberOfOnes = changeTen // 1
print(numberOfOnes)