      
def ask_money(currency, money):
    while True:
        currency = input("Enter the curreny: ").upper()
        if len(currency) < 1 or currency.isdigit():
            print("***Enter a valid currency!!!")
            continue
        else:
            break
    while True:
        money = input(f"Enter the amount of money: {currency} ")
        if not money.isdigit():
            print("***Enter a valid amount of money!!!")
            continue
        else:
            break
    return currency, money

def format_currency(money, result):
    index = 0
    result = ""
    for digit in money[::-1]:
        index += 1
        result += digit
        if index % 3 == 0:
            result += ","
    if result[-1::] == ",":
        result = result[-2::-1]
    else:
        result = result[::-1]
    
    return result



def display_result(currency, money, result):
    print()
    print("******************************* RESULT *******************************")
    print(f"The amount of money you entered: {money}")
    print(f"The formatted currency is: {currency} {result}")
    print("**********************************************************************")
    print()

def main():
    currency = ""
    money = ""
    result = ""
    is_running = True

    print("------------------- CURRENCY FORMATTER -------------------")
    print()

    while is_running:
        currency, money = ask_money(currency, money)
        result = format_currency(money, result)
        display_result(currency, money, result)
        while True:
            ask_restart = input("Do you want to format another currency as well? (Y or N): ").upper()
            if ask_restart not in ("Y", "N"):
                print("INVALID INPUT!!!")
                continue
            elif ask_restart == "Y":
                print()
                break
            else:
                is_running = False
                break
        



if __name__ == '__main__':
    main()