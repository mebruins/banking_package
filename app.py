# Bonus Task Infinite - I added the option of a savings and checking account for each menu option.
# I had to double number of functions in account.py to match the needs of app.py options

from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print('        ========  Automated Teller Machine  ========        ')


while True:
    name = input('Enter name to register: ')
    pin = input('Enter PIN: ')
    if len(name) > 10:
        print('Maximum name length is 10 characters. Please try again')
        continue
    elif len(pin) > 4:
        print('Maxim PIN length is 4 characters. Please try again')
        continue
    else:
        break


while True:
    name_to_validate = input('Enter name: ')
    pin_to_validate = input('Enter PIN: ')
    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful')
        break
    else:
        print('Invalid credentials')

savings_balance = 0.0
checking_balance = 0.0
print(name, 'has a savings balance of $' + str(savings_balance))
print(name, 'has a checking balance of $' + str(checking_balance))

while True:
    atm_menu(name)
    option = input('Choose an option: ')
    if option == '1':
        acc_option = input('1-Savings or 2-Checking: ')
        if acc_option == '1':
            account.show_savings_balance(savings_balance)
        elif acc_option == '2':
            account.show_checking_balance(checking_balance)

    elif option == '2':
        acc_option = input('1-Savings or 2-Checking: ')
        if acc_option == '1':
            savings_balance = account.deposit_savings(savings_balance)
            print('Savings:', savings_balance)
            print('Checking:', checking_balance)
        elif acc_option == '2':
            checking_balance = account.deposit_checking(checking_balance)
            print('Savings:', savings_balance)
            print('Checking:', checking_balance)

    elif option == '3':
        acc_option = input('1-Savings or 2-Checking: ')
        if acc_option == '1':
            savings_balance = account.withdraw_savings(savings_balance)
            print('Savings:', savings_balance)
            print('Checking:', checking_balance)
        elif acc_option == '2':
            checking_balance = account.withdraw_checking(checking_balance)
            print('Savings:', savings_balance)
            print('Checking:', checking_balance)

    elif option == '4':
        account.logout(name)
        break
