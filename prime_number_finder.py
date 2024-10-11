print("Welcome to Prime Number Identifier")
number = int(input("Enter a number: "))

if number > 5 and number % 6 == int(1 or 5):
    print(number, "is a prime number") 

elif number == int(2 or 3 or 5):
    print(number, "is a prime number")

elif number <= 1:
    print(number, "is neither a prime number or a composite number")

else:
    print(number, "is a composite number" )