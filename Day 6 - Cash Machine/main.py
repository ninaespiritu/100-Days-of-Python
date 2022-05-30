print("Welcome to the Cash Machine.\n")

# Function: Withdraw after successful PIN
def withdraw():
  account_balance = 12_800
  input_withdraw = float(input("Please enter the amount you would like to withdraw: "))

  if input_withdraw <= account_balance:
    account_balance -= input_withdraw
    print(f"\nYou have successfully withdrawn £{input_withdraw}. Your new balance is £{account_balance}.")
  else:
    print(f"\nSorry, you do not have enough balance. Your current balance is £{account_balance}.")
    withdraw()

# Function: Comparing PIN
def pin():
  account_pin = 1234
  input_pin = int(input("Enter your PIN: "))

  if input_pin == account_pin:
    print("\nPIN successful.")
    withdraw()
  else:
    print("\nIncorrect PIN. Please try again.")
    pin()

pin()