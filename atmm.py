def atm_transaction():
    # Initial balance stored in the system
    balance = 5000.00
    print(f"Current Balance: ₹{balance}")
try:
        # Taking withdrawal amount as input
        amount = int(input("Enter the amount to withdraw (multiples of 100): "))

        # Validation 1: Check if amount is a multiple of 100
        if amount % 100 != 0:
            print("Error: Amount must be a multiple of 100 (e.g., 100, 200, 500).")