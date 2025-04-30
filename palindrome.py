

def palindrome():
    print("\n\n----------PALINDROME CHECKER ---------\n")

    mode = input("Which data type do you want to enter? (N for number and S for string): ").upper()
    while True:
        if mode not in ("N", "S"):
            mode = input("INVALID INPUT! Enter N or S: ").upper()
        else:
            break

    if mode == "N":
        number = input("Enter a number: ")
        while True:
            if number.isdigit():
                number = int(number)
                break
            else:
                number = input("*****Enter a valid number: ")
        a = number
        s = 0
        while a != 0:
            r = a % 10
            s = s * 10 + r
            a = int(a / 10)
        if s == number:
            print(f"{number} is palindrome.")
        else:
            print(f"{number} is not palindrome.")

    else:
        string = input("Enter a string: ")
        while True:
            if len(string) >= 1:
                break
            else: 
                string = input("*****Enter a valid string: ")
        reversed_string = string[::-1]
        if reversed_string == string:
            print(f"{string} is palindrome")
        else:
            print(f"{string} is not palindrome")

while True:
    palindrome()
    ask_another = input("Do you want to restart? (Y or N): ").upper()
    while True:
        if ask_another not in ("Y", "N"):
            ask_another = input("INVALID INPUT! Enter  Y or N: ")
        else:
            break
    if ask_another == "Y":
        continue
    else:
        print("BYE!👋")
        break


