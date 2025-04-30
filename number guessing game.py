import random
ask_restart = ""

def num_guess_game():
    min_value = 1

    print("\n\n---------- NUMBER GUESSING GAME ---------\n")

    diff_level = input("Enter a level of difficulty (EASY, MEDIUM, HARD): ").upper()
    while True:
        if diff_level not in ("EASY", "MEDIUM", "HARD"):
            diff_level = input("INVALID INPUT! Enter EASY, MEDIUM or HARD: ").upper()
        else:
            break
    if diff_level == "EASY":
        max_value = 10
    elif diff_level == "MEDIUM":
        max_value = 50
    else:
        max_value = 100

    random_num = random.randint(min_value, max_value)


    user_guess = input(f"Enter a number ({min_value} - {max_value}): ")
    while not user_guess.isdigit():
        user_guess = input("****Enter a valid number: ")
    user_guess = int(user_guess)
    attempts = 1

    while not user_guess == random_num:
        attempts += 1
        if user_guess > random_num:
            print("You guessed TOO HIGH!")
        elif user_guess < random_num:
            print("You guessed TOO LOW!")
        user_guess = input(f"Enter a number ({min_value} - {max_value}): ")
        while True:
            if user_guess.isdigit():
                user_guess = int(user_guess)
                break
            else:
                user_guess = input("****Enter a valid number: ")

    print(f"CONGRATULATIONS! You've guessed the right no.: {random_num} in {attempts} attempts")    

# while not ask_restart.upper() == "N":
#      num_guess_game()
#      ask_restart = input("Do you want to play again? (Y or N): ")  
#      if ask_restart.upper() != "Y":
#         print("Thanks for playing! 👋")
#         break
    
while True:
    num_guess_game()
    ask_restart = input("Do you want to play again? (Y or N): ").upper()
    while ask_restart not in ("Y", "N"):
        ask_restart = input("INVALID INPUT! Enter Y or N: ").upper()
    if ask_restart == "N":
        print("Thanks for playing! 👋")
        break
    else:
        continue

        