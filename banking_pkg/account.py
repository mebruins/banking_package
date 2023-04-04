def show_savings_balance(savings_balance):
    print("Current savings: $" + str(savings_balance))


def show_checking_balance(checking_balance):
    print("Current checking: $" + str(checking_balance))


def deposit_savings(savings_balance):
    dep = input('Amount to deposit: ')
    balance = savings_balance + float(dep)
    return balance


def deposit_checking(checking_balance):
    dep = input('Amount to deposit: ')
    balance = checking_balance + float(dep)
    return balance


def withdraw_savings(savings_balance):
    withdraw = input('Amount to withdraw: ')
    if int(withdraw) > savings_balance:
        print("You don't have that kind of cash!!")
        return savings_balance
    else:
        balance = savings_balance - float(withdraw)
        return balance


def withdraw_checking(checking_balance):
    withdraw = input('Amount to withdraw: ')
    if int(withdraw) > checking_balance:
        print("You don't have that kind of cash!!")
        return checking_balance
    else:
        balance = checking_balance - float(withdraw)
        return balance


def logout(name):
    print('Goodbye', name)
