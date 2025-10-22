# Function to calculate total bill amount
def calculate_total_bill(amount, tax_rate, discount):
    """
    Calculates total amount after applying tax and discount.
    """
    tax = amount * tax_rate / 100
    total = amount + tax - discount
    return total

# Main program
print("🧾 Restaurant Billing System 🧾")
amount = float(input("Enter the bill amount: ₹"))
tax_rate = float(input("Enter tax rate (%): "))
discount = float(input("Enter discount amount: ₹"))

total = calculate_total_bill(amount, tax_rate, discount)
print(f"\nTotal amount to be paid: ₹{total:.2f}")




#2# Simple ATM System Function to check balance

def check_balance(balance):
    print(f"Your current balance is: ₹{balance:.2f}")

def deposit(balance, amount):
    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    return balance

# Main program
balance = 1000.00  # Starting balance
while True:
    print("\n🏧 Simple ATM Menu 🏧")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance = deposit(balance, amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        balance = withdraw(balance, amount)
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

