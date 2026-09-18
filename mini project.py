balance = 1000.0  # Initial default balance
pin = "1234"


def check_balance():
    print(f"\nCurrent balance: ${balance:.2f}\n")


def deposit():
    global balance
    amount = float(input("\nEnter amount to deposit: $"))
    if amount > 0:
        balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}\n")
    else:
        print("Invalid deposit amount.\n")


def withdraw():
    global balance
    amount = float(input("\nEnter amount to withdraw: $"))
    if amount <= 0:
        print("Invalid withdrawal amount.\n")
    elif amount > balance:
        print("Insufficient balance.\n")
    else:
        balance -= amount
        print(f"Withdrawn ${amount:.2f}. New balance: ${balance:.2f}\n")


def main():
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin != pin:
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select from 1 to 4.\n")


if __name__ == "__main__":
    main()