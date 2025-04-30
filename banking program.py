


def show_balance(balance):
    print(f"Your balance is NRs.{balance:.2f}")
    print()

def deposit():
    amount = ""

    while True:
        amount = input("Enter an amount to be deposited: Nrs.")
        if not amount.isdigit():
            print("INVALID INPUT!")
        elif float(amount) < 0:
            print("INVALID INPUT!")
        else:
            amount = float(amount)
            print()
            break
    
    return amount

def withdraw(balance):
    amount = ""

    while True:
        amount = input("Enter an amount to be withdrawed: Nrs.")
        if not amount.isdigit():
            print("INVALID INPUT!")
        elif float(amount) < 0:
            print("INVALID INPUT!")
        elif float(amount) > balance:
            print("You don't have enough balanace!")
            amount = float(amount)
            amount = 0
            print()
            break
        else:
            amount = float(amount)
            print()
            break
    
    return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------- BANKING PROGRAM ----------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        while choice not in ("1", "2", "3", "4"):
            choice = input("*****Please enter a valid choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        else:
            is_running = False

    print("BYE!👋")

main()

if __name__ == '__main__':
    main()