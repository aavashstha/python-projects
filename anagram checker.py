ask_restart = ""


def anagram():

    letters = []


    print("---------- ANAGRAM CHECKER ----------")
    print()

    #asking for the letters
    while True:
        first_word = input("Enter the first word: ")
        if not first_word.isalpha():
            print("INVALID INPUT! Please provide a valid word!!!")
            continue
        else:
            break
    while True:
        second_word = input("Enter the second word: ")
        if not second_word.isalpha():
            print("INVALID INPUT! Please provide a valid word!!!")
            continue
        elif len(first_word) != len(second_word):
            print("The length of the first and the second word must be same! ")
            continue
        else:
            break
    


    #ading letters from first word to list of letters
    for letter_first in first_word:
        letters.append(letter_first.upper())
    
    #checking if letter of second word contain the letter from list of letters
    for letter_second in second_word:
        if letter_second.upper() not in letters:
            is_anagram = False
            break
        else:
            letters.remove(letter_second.upper())
            is_anagram = True
        

    if is_anagram:
        print(f"The words {first_word} and {second_word} are anagram!")
    else:
        print(f"The words {first_word} and {second_word} are not anagram!")
        


while True:
    anagram()
    while ask_restart not in ("Y", "N"):
        ask_restart = input("Do you want to continue: (Y or N): ").upper()
    if ask_restart == "Y":
        ask_restart = ""
        continue
    else:
        print("BYE!👋")
        break