
# Printing what the program will do
print("Hi there I will ditermine if your Integer is a odd or even number")
# User input
number = input("You number here: ")

# Determining is the code is an integer or not
# if not try again until it's an number
while (not number.isdigit()):
    number = input("You number here: ")

# Conversion
number = int(number)

# Equation
answer = number % 2

if (answer == 0):
    print("Even")
else:
    print("Odd")


    