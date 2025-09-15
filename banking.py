# banking.py - Professional console version with transaction history
import datetime

balance = 0
history_file = "transactions.txt"

def log_transaction(action, amount=None):
    """Save each action to transactions.txt with timestamp"""
    with open(history_file, "a") as f:
        time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if amount is not None:
            f.write(f"[{time_str}] {action}: {amount} | Balance: {balance}\n")
        else:
            f.write(f"[{time_str}] {action} | Balance: {balance}\n")

def check_balance():
    print("Total balance:", balance)
    log_transaction("Checked Balance")

def cash_withdraw(w_amt):
    global balance
    try:
        w_amt = int(w_amt)
    except:
        print("Invalid withdraw amount")
        return
    if w_amt <= 0:
        print("Enter amount > 0")
        return
    if balance < w_amt:
        print("Insufficient Balance")
        log_transaction("Failed Withdraw", w_amt)
    else:
        balance -= w_amt
        print(f"{w_amt} Rs successfully Withdrawn")
        log_transaction("Withdraw", w_amt)

def cash_deposit(d_amt):
    global balance
    try:
        d_amt = int(d_amt)
    except:
        print("Invalid deposit amount")
        return
    if d_amt <= 0:
        print("Enter amount > 0")
        return
    balance += d_amt
    print(f"{d_amt} Rs deposited Successfully")
    log_transaction("Deposit", d_amt)

def show_history():
    try:
        with open(history_file, "r") as f:
            print("\n=== Transaction History ===")
            print(f.read())
    except FileNotFoundError:
        print("No history available yet.")

def reset_account():
    global balance
    balance = 0
    print("Account reset. Balance is 0.")
    log_transaction("Account Reset")

def main():
    while True:
        try:
            ch = int(input(
                "\nEnter your choice:\n"
                "1. Deposit Cash\n"
                "2. Withdraw Cash\n"
                "3. Check Balance\n"
                "4. Show Transaction History\n"
                "5. Reset Account\n"
                "6. Exit\n> "
            ))
        except ValueError:
            print("Invalid Input")
            continue

        if ch == 1:
            try:
                amt = int(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid amount")
                continue
            cash_deposit(amt)
            check_balance()

        elif ch == 2:
            try:
                amt = int(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid amount")
                continue
            cash_withdraw(amt)
            check_balance()

        elif ch == 3:
            check_balance()

        elif ch == 4:
            show_history()

        elif ch == 5:
            reset_account()

        elif ch == 6:
            print("Exit. Thank you for banking with us!")
            break

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
