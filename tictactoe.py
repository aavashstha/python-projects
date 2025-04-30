import random

def game_board(user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves):
    for i in range(9):
        if i %3 == 0:
            print()

        if str(i) in list_of_user1_moves:
            print(user1_symbol, end="  ")
        elif str(i) in list_of_user2_moves:
            print(user2_symbol, end="  ")
        else:
            print(i, end="  ")
    print()


def score_board(user1_score, user2_score):
    print()
    print("★ ★ ★ ★ ★ ★ ★ SCORE BOARD ★ ★ ★ ★ ★ ★ ★")
    print(f"USER1: {user1_score}")
    print(f"USER2: {user2_score}")
    print("꒷꒦︶꒷꒦︶꒷꒦︶꒷꒦︶꒷꒦︶꒷꒦︶꒷꒦")
    print()


def check_winner(options, user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves, is_running, user1_score, user2_score):
    win_conditions = [["0", "1", "2"],
                      ["3", "4", "5"],
                      ["6", "7", "8"],
                      ["0", "3", "6"],
                      ["1", "4", "7"],
                      ["2", "5", "8"],
                      ["0", "4", "8"],
                      ["2", "4", "6"]]
    
    if options == []:
        print("IT'S A DRAW!🤝")
        is_running = False
    else:
        user1_wins = False
        user2_wins = False
        for condition in win_conditions:
            if all(move in list_of_user1_moves for move in condition):
                user1_wins = True
                break
            elif all(move in list_of_user2_moves for move in condition):
                user2_wins = True
                break
        if user1_wins:
            print(f"CONGRATULATIONS! {user1_symbol} WINS!🎉")
            print(f"SORRY! {user2_symbol} LOSES!☹️")
            user1_score += 1
            score_board(user1_score, user2_score)
            is_running = False

        elif user2_wins:
            print(f"CONGRATULATIONS! {user2_symbol} WINS!🎉")
            print(f"SORRY! {user1_symbol} LOSES!☹️")
            user2_score += 1
            score_board(user1_score, user2_score)
            is_running = False

    return is_running, user1_score, user2_score  



def game(options, occupied_options, user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves, user1_score, user2_score):
    options = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    occupied_options = []
    is_running = True
    symbols = ("X", "O")

    #choosing symbol for both the users
    user1_symbol = random.choice(symbols)
    match(user1_symbol):
        case "X":
            user2_symbol = "O"
        case "O":
            user2_symbol = "X"

    while is_running:
        print()
        #asking for the move of user1:
        while True:
            if is_running:
                user1_move = input("USER 1. Enter a valid move from 0-8: ")
                if user1_move not in ("0", "1", "2", "3", "4", "5", "6", "7", "8"):
                    print("***Please enter a valid number from 0-8!!!")
                    continue
                elif user1_move in occupied_options:
                    print("***SPACE ALREADY OCCUPIED!!!")
                    continue
                else:
                    options.remove(user1_move)
                    occupied_options.append(user1_move)
                    list_of_user1_moves.append(user1_move)
                    game_board(user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves)
                    is_running, user1_score, user2_score = check_winner(options, user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves, is_running, user1_score, user2_score)
                    break
            else:
                break

        #asking for the move of user2
        while True:
            if is_running:
                user2_move = input("USER 2. Enter a valid move from 0-8: ")
                if user2_move not in ("0", "1", "2", "3", "4", "5", "6", "7", "8"):
                    print("***Please enter a valid number from 0-8!!!")
                    continue
                elif user2_move in occupied_options:
                    print("***SPACE ALREADY OCCUPIED!!!")
                    continue
                else:
                    options.remove(user2_move)
                    occupied_options.append(user2_move)
                    list_of_user2_moves.append(user2_move)
                    game_board(user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves)
                    is_running, user1_score, user2_score = check_winner(options, user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves, is_running, user1_score, user2_score)
                    break
            else:
                break

    return user1_score, user2_score


def main():

    user1_score = 0
    user2_score = 0
    ask_restart = "Y"

    print()
    print("---------- TIC TAC TOE ----------")

 


    while ask_restart == "Y":
        user1_symbol = ""
        user2_symbol = ""
        options = []
        occupied_options = []
        list_of_user1_moves = []
        list_of_user2_moves = []
        #displat initial board:
        for i in range(9):
            if i %3 == 0:
                print()
            print(i, end = "  ")
        print()

        user1_score, user2_score = game(options, occupied_options, user1_symbol, user2_symbol, list_of_user1_moves, list_of_user2_moves, user1_score, user2_score)

        while True:
            ask_restart = input("Do you want to play again? (Y or N): ").upper()
            if ask_restart not in ("Y", "N"):
                print("INVALID INPUT!!!")
                continue
            elif ask_restart == "N":
                print("Thanks for playing!✌️")
                break
            else:
                break
    

if __name__ == '__main__':
    main()
     