import datetime

# Time that gets displayed
x = datetime.datetime.now()
print("The time is:")
print(x.strftime("%a %d %b %I %M %p"))


# Name that the user chooses gets judged
name = input("Please enter your name: ")

name = name.lower()

if name == "geoff":
    print("G'day Geoff")
else:
    print("Wait a minute you're not Geoff")