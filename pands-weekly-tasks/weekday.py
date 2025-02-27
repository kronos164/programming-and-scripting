import datetime

# Get the current date and time
time_now = datetime.datetime.now()

# Get the current day of the week
day = time_now.weekday()

if day < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
    
# References:
# https://docs.python.org/3/library/datetime.html