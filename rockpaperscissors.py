import random

moves = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

print("----- ROCK PAPER SCISSORS -----")

while True: 

    player_move = input("Enter your move (rock / paper / scissors) (enter 'q' to quit): ").lower()


    if player_move == "q":
        print("Thanks for playing! 👋")
        break
    

    if player_move not in moves:
        print("Please enter a valid move!!! (rock / paper / scissors)")
        continue


      
    computer_move = random.choice(moves)
    if player_move == computer_move:
        player_score +=1
        computer_score +=1
        print(f"You chose {player_move} and computer also chose {computer_move}.\nIT'S A TIE!")
        print(f"Computer Score: {computer_score}")
        print(f"Your Score: {player_score}")
    elif (computer_move == "rock" and player_move == "scissors") or (computer_move == "paper" and player_move == "rock") or (computer_move == "scissors" and player_move == "paper"):
        computer_score += 1  
        print(f"You chose {player_move} and computer chose {computer_move}.\nYOU LOSE!")
        print(f"Computer Score: {computer_score}")
        print(f"Your Score: {player_score}")
    else:
        player_score +=1
        print(f"You chose {player_move} and computer chose {computer_move}.\n YOU WIN!") 
        print(f"Computer Score: {computer_score}")
        print(f"Your Score: {player_score}")