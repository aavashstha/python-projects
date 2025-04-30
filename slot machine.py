import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋," "🔔", "⭐"]
    results = []

    for _ in range(3):
        results.append(random.choice(symbols))

    return results

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
    
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    else:
        return 0
    

def main():
    balance = 100
    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance > 0:
        print()
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("INSUFFICIENT FUNDS!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0!")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        if balance > 0:
            while True:
                play_again = input("Do you want to spin again? (Y or N): ").upper()
                if play_again not in ("Y", "N"):
                    print("INVALID INPUT!")
                    continue
                elif play_again == "Y":
                    break
                else:
                    display_balance = balance
                    balance = 0
                    break
    
    print()
    print("********************************************")
    print(f"Game over! Your final balance is ${display_balance}")
    print("Thanks for playing! BYE👋")
    print("********************************************")                

if __name__ == '__main__':
    main()


