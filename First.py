import time
#this is used for load account from the accounts.txt
def load_accounts():
    accounts = {}
    with open('account.txt', 'r') as file:
        for line in file:
            account_number,pin,balance = line.strip().split(',')
            accounts[account_number] = {'pin': int(pin), 'balance': int(balance)}
    return accounts
#this is used for save accounts in the accounts.txt that wht ypu updated in your balance and pin
def save_accounts(accounts):
    with open('account.txt', 'w') as file:
        for account_number, info in accounts.items():
            file.write(f"{account_number},{info['pin']},{info['balance']}\n")
#this is for change password
def change_password(account_number, accounts):
    current_pin = int(input("Enter your current PIN: "))
    if current_pin == accounts[account_number]['pin']:
        new_pin = int(input("Enter your new PIN: "))
        confirm_pin = int(input("Confirm your new PIN: "))
        if new_pin == confirm_pin:
            accounts[account_number]['pin'] = new_pin
            save_accounts(accounts)
            print("Your PIN has been successfully changed.\n")
        else:
            print("PINs do not match. Please try again.\n")
    else:
        print("Incorrect current PIN. Please try again.\n")
    time.sleep(2)
#this is the main atm menu 
def atm_menu(account_number, accounts):
    while True:
        print("1. Check Your Bank Balance\n")
        print("2. Withdraw Money \n")
        print("3. Deposit Money \n")
        print("4. Change Password \n")
        print("5. Exit\n")
        option = int(input("Enter The Option (1,2,3,4 or 5): "))
        
        if option == 1:
            print(f"Your Current Balance is {accounts[account_number]['balance']}\n")
            time.sleep(2)
        elif option == 2:
            withdraw = int(input("Enter Amount You Want to Withdraw: "))
            if withdraw > accounts[account_number]['balance']:
                print("INSUFFICIENT BALANCE\n")
                time.sleep(2)
            else:
                accounts[account_number]['balance'] -= withdraw
                print(f"Your Updated Balance is: {accounts[account_number]['balance']}\n")
                time.sleep(2)
                
        elif option == 3:
            deposit = int(input("Enter Amount You Want to Deposit: "))
            accounts[account_number]['balance'] += deposit
            print(f"Your Updated Balance is: {accounts[account_number]['balance']}\n")
            time.sleep(2)

        elif option == 4:
            change_password(account_number,accounts)
            
        elif option == 5:
            save_accounts(accounts)
            print("Thank you for using our ATM. Goodbye!")
            exit(0)
        else:
            print("Invalid option, please try again.")


def main():
    accounts = load_accounts()
    print("---PLEASE INSERT YOUR CARD---\n\n")
    time.sleep(2)
    
    account_number = input("Enter Your Account Number: ")
    if account_number in accounts:
        pin = int(input("Enter Your PIN: "))
        if pin == accounts[account_number]['pin']:
            atm_menu(account_number, accounts)
        else:
            print("WRONG PIN!!!")
    else:
        print("Account number not found.")

if __name__ == "__main__":
    main()
