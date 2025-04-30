import time

def game():
        

    questions = ("What is the capital city of Nepal?",
                "Who was the last king of the Shah Dinestiy?",
                "What is the national color of Nepal?",
                "Who is known as the creator of the modern Nepal?",
                "How many elements are there in the Mendeleev's periodic table")

    options = (("A. Pokhara", "B. Bhaktapur", "C. Kathmandu", "D.Lalitpur"),
            ("A. King Prithvi Narayan Shah", "B. King Mahendra Shah", "C. King Birendra Shah", "D. King Gyanendra Shah"), 
            ("A. Crimson", "B. Blue", "C. Indigo", "D. Red"), 
            ("A. King Tribhuvan Shah", "B. King Prithvi Narayan Shah", "C. King Pratap Malla", "D. King Mahendra Shah"), 
            ("A. 118", "B. 63", "C. 68", "D. 120"))

    answers = ("C", "D", "A", "B", "B")
    guesses = []
    score = 0
    question_num = 0
    for question in questions:
        print("-------------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A, B, C, D): ").upper()
        while guess not in ("A", "B", "C", "D"):
            guess = input("Invalid response! Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer!")
        print(f"Score: {score}")
        question_num += 1
        time.sleep(0.25)
    
    time.sleep(1)
    print("\nCALCULATING RESULTS.", end = "")
    time.sleep(0.5)
    print(".", end = "")
    time.sleep(0.5)
    print(".", end = "")
    time.sleep(0.5)
    print(".", end = "")
    time.sleep(0.5)
    print(".", end = "")
    time.sleep(0.5)
    print(".", end = "")
    time.sleep(0.5)
    print(".")

    print("\n---------------------------------")
    print("             RESULTS             ")
    print("---------------------------------")

    print("\nAnswers: ", end = "")
    for answer in answers:
        print(answer, end = " ")


    print("\nGuesses: ", end = "")
    for guess in guesses:
        print(guess, end = " ")

    score_percentage = int((score / len(questions) ) * 100)

    print(f"\n\nThe final score is: {score}\nYou've scored {score} out of {len(questions)} which is {score_percentage}%!\n\n")

while True:
    game()
    restart_game = input("Do you want to restart? (Y or N): ").upper()

    if restart_game == "Y":
        continue
    else:
        print("Thanks for playing!👋")
        break