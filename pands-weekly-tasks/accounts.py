# Read in a user's account number
account_n = input("Enter your account number: ")

# Mask the account number
masked_account_n = 'X' * (len(account_n) - 4) + account_n[-4:]

# Print the masked account number
print("Your masked account number is: " + masked_account_n)