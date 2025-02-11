# Imputs two amounts in cents
amount_1 = input("Enter 1st amount(in cents): ")
amount_2 = input("Enter 2nd amount(in cents): ")

# Calculate the total amount in euro
total = (int(amount_1) + int(amount_2)) / 100
total = "{:.2f}".format(total)

# Print the total amount
print("The total amount is: €" + str(total))