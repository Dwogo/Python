import datetime

x = datetime.datetime.now()


print(" The time is:")
print(x.strftime("%a %d %b %I %M %p"))

name = input("Please enter your name: ")

if name == "Geoff":
    print("G'day Geoff")
else:
    print("Wait a minute you're not Geoff")