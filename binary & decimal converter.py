import time
ask_restart = ""

def number_converter():
    print("---------- NUMBER CONVERTER ----------\n")

    #conversion mode select
    while True:
        mode = input("Enter a mode for your number to be converted (B for binary and D for decimal): ").upper()
        if mode not in ("B", "D"):
            print("INVALID INPUT!")
            continue
        else:
            break

    #asking for the number:
    text_validation = False
    final_number = 0
    if mode == "D":
        #number validation
        while not text_validation:
            initial_number = input("Enter the binary number: ")
            for digit in initial_number:
                if digit not in ("0", "1"):
                    print(f"{initial_number} is not a binary number!")
                    text_validation = False
                    break
                else:
                    text_validation = True
                    continue
        #conversion to deimal
        exponent = 0
        reversed_initial = initial_number[::-1]
        for digit in reversed_initial:
            digit = int(digit)
            final_number += (digit * pow(2, exponent))
            exponent += 1
        #output
        print()
        time.sleep(1)
        print("CALCULATING RESULTS", end = "")
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
        print()
        print("--------------- RESULT ----------")
        print(f"The converted decimal number of {initial_number} is: {final_number}")
    
    else:
        #text validation
        while not text_validation:
            initial_number = input("Enter the decimal number: ")
            if not initial_number.isdigit():
                print("INVALID INPUT!")
                text_validation = False
                continue
            else:
                text_validation = True
        
        #number conversion
        output_initial_number = initial_number
        final_number = ""
        initial_number = int(initial_number)
        while not initial_number <= 0:
            final_number += str(initial_number % 2) 
            initial_number = int(initial_number / 2)
            
        final_number = final_number[::-1]
        #output
        print()
        time.sleep(1)
        print("CALCULATING RESULTS", end = "")
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
        print()
        print("--------------- RESULT ----------")
        print(f"The converted decimal number of {output_initial_number} is: {final_number}")
                    
               
        

while True:
    number_converter()
    while ask_restart not in ("Y", "N"):
        ask_restart = input("Do you want to convert any other number? (Y or N): ").upper()
    if ask_restart == "Y":
        ask_restart = ""
        print()
        continue
    else:
        print("BYE!👋")
        break
                    