balance = 1000

def atm_menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")



while True:
    atm_menu()

    try:
        user_input = int(input("Please make a choice: 1, 2, 3, 4: "))
        if user_input not in [1, 2, 3, 4]:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue
    except ValueError:
        print("Incorrect input. Please enter a number between 1 and 4.")
        continue

    if user_input == 1: 
        print(f"Current bank balance ${balance:.2f}")

    elif user_input == 2: 
        try:
            deposit_amount = float(input("Please enter deposit amount: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Updated bank balance is ${balance:.2f}")
            else: 
                print("Please enter a postive amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    elif user_input == 3: 
        try:
            withdraw_amount = float(input("Please enter withdraw amount: "))
            if withdraw_amount > 0:
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Updated bank balance is ${balance:.2f}")
                else: 
                    print("Insufficient funds.")
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif user_input == 4: 
        print("Thank you for using the Smart ATM. Goodbye!")
        break


