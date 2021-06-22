
guesses = 0
total = 0

number = int(input("Guess a number "))
guesses = guesses + 1

while (not number == 0):
    total = total + number
    number = int(input("Guess a number "))
    guesses = guesses + 1

print ("You guessed " + str(guesses) + " times")
print("The total sum is " + str(total))