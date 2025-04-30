
import random

def ask_info():
    while True:
        password_length = input("Enter the length for your password (8-20): ")
        if not password_length.isdigit():
            print("***Enter a valid number!!!")
            continue
        elif int(password_length) < 8:
            print("Password must be at least 8 characters long!")
            continue
        elif int(password_length) > 20:
            print("Password must be at most 20 characters long!")
            continue
        else:
            password_length = int(password_length)
            break
    
    list_of_include_chars = []
    
    print()
    print("1. Uppercase Alphabets")
    print("2. Lowercase Alphabets")
    print("3. Digits")
    print("4. Symbols")
    print("5. Quit")
    while True:
        if list_of_include_chars == ["1", "2", "3", "4"]:
            print("You've decided to add all types of character.")
            break
        else:
            include_chars = input("Keep on entering the chars you want from 1 - 4(5 to quit): ")
            if include_chars not in ["1", "2", "3", "4", "5"]:
                print("***Please enter a valid number!!!")
                continue
            elif include_chars in list_of_include_chars:
                print("You've already included this character type!!!")
                continue
            elif include_chars == "5":
                if list_of_include_chars == []:
                    print("***Enter atlest one type of character!!!")
                elif len(list_of_include_chars) < 2:
                    print("**Please choose ate least two character types!!!")
                    continue
                else:
                    break
            else:
                list_of_include_chars.append(include_chars)
                continue
            

    return password_length, list_of_include_chars


def generate_password(password_length, list_of_include_chars):
    password = ""
    list_of_chars = []
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~']

    for char in list_of_include_chars:
        if char == "1":
            for i in range(65,91):
                list_of_chars.append(chr(i))
        elif char == "2":
            for i in range(97,123):
                list_of_chars.append(chr(i))
        elif char == "3":
            for i in range(48, 58):
                list_of_chars.append(chr(i))
        else:
            for symbol in symbols:
                list_of_chars.append(symbol)


    for length in range(password_length):
        password += random.choice(list_of_chars)

    return password


def display_password(password):
    print()
    print("********************")
    print(f"PASSWORD: {password}")
    print("********************")
    print()


def main():
    is_running = True

    print("---------- PASSWORD GENERATOR ---------")
    print()

    while is_running:
        password_length, list_of_include_chars = ask_info()
        password = generate_password(password_length, list_of_include_chars)
        display_password(password)
        while True:
            ask_restart = input("Do you want to generate another password as well? (Y or N): ").upper()
            if ask_restart not in ("Y", "N"):
                print("INVALID INPUT!!!")
                continue
            elif ask_restart == "Y":
                break
            else:
                print("BYE!👋")
                is_running = False
                break
                

if __name__ == '__main__':
    main()