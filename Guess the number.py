
guesses = 0
total = 0

number = int(input("Guess a number "))
guesses = guesses + 1
total = total + number

while (not number == 0):
    number = input("Guess a number ")
    total = total + int(number)
    guesses = guesses + 1

print ("You guessed " + str(guesses) + " times")
print("The total sum is " + str(total))