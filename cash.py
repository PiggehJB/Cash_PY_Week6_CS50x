import colorama
from colorama import Fore


while True:
    try:
        cash = float(input("Enter your cash: "))
        while True:
            if cash > 0:
                print(f"Alright! Your balance is: {cash}")
                break
            else:
                cash = float(input(f"{Fore.RED}Uh oh! Make sure your number is above 0: {Fore.CYAN}"))
        break
    except ValueError:
        print("Uh oh! That wasn't a valid number, please try again.")


amount_of_coins = 0

while True:
    if cash == 0:
        print(f"{Fore.GREEN}\n\nDone calculating change...\nAmount of Coins: {amount_of_coins}\nRemaining change: ${cash}")
        break

    if cash >= 0.25:
        cash -=0.25
        cash = round(cash, 2)
        amount_of_coins +=1
        print(f"{Fore.CYAN}Diving by quarters\nAmtOfCoins: {amount_of_coins}\nRemaining change {cash}")

    
    elif cash >= 0.10 and cash < 0.25:
        cash -=0.1
        """
        TLDR; computers represent floating point numbers as binary, and it turns out that storing 
        a precise decimal fraction as binary is not possible
        """
        cash = round(cash, 2)
        amount_of_coins +=1
        print(f"{Fore.BLUE}\nDiving by dimes\nAmtOfCoins: {amount_of_coins}\nRemaing change: {cash}")

    elif cash >=0.05 and cash < 0.10:
        cash -=0.05
        cash = round(cash, 2)
        amount_of_coins +=1
        print(f"{Fore.YELLOW}\nDiving by nickels\nAmtOfCoins: {amount_of_coins}\nRemaing change: {cash}")

    elif cash >=0.01 and cash < 0.05:
        cash -=0.01
        cash = round(cash, 2)
        print(f"{Fore.YELLOW}\nDiving by pennies\nAmtOfCoins: {amount_of_coins}\nRemaing change: {cash}")
        amount_of_coins +=1

print(f"{Fore.RED}\n\nRounded the numbers to 2 decimal places\n")