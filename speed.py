
# Input for the user
unit = input("Is it in kilometers or meters? ")
unit = unit.lower()
distance = float(input("What is the distance? "))
time = float(input("How long did it take in seconds? "))

if (unit == "kilometer" or unit == "kilometers" or unit == "kilometres" or unit == "kilometre" or unit =="km"):
    answer = distance/time
    answer = str(answer)
    print(answer + "km/s")
elif (unit == "meter" or unit == "metre" or unit == "meters" or unit == "metres" or unit == "m"):
    answer = distance/time
    answer = str(answer)
    print(answer + "m/s")
else:
    print("Sorry I can only do meters and kilometers")