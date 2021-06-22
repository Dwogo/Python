

# Asking the user how many pounds do they have
pounds = input("How many pounds do you have? ")
while (not pounds.isdigit()):
    pounds = input("How many pounds do you have? ")

#Convert string into float
pounds = float(pounds)


# Exchange rate of pounds to euros (2021)
exchange = 1.16
Euros = pounds * exchange
# Why not
print("{:.2f}€".format(Euros))


day_spend = Euros/4
print("{:.2f}€ per day".format(day_spend))