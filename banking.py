# banking.py - console version
balance = 0

def check_balance():
    print("Total balance:", balance)

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
    else:
        balance -= w_amt
        print(f"{w_amt} Rs successfully Withdrawn")

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

def main():
    while True:
        try:
            ch = int(input("\nEnter the choice:\n1.Deposit Cash\n2.Withdraw cash\n3.Check balance\n4.Exit\n"))
        except ValueError:
            print("Invalid Input")
            continue

        if ch == 1:
            try:
                amt = int(input("enter amount to deposit: "))
            except ValueError:
                print("Invalid amount")
                continue
            cash_deposit(amt)
            check_balance()
        elif ch == 2:
            try:
                amt = int(input("enter amount to withdraw: "))
            except ValueError:
                print("Invalid amount")
                continue
            cash_withdraw(amt)
            check_balance()
        elif ch == 3:
            check_balance()
        elif ch == 4:
            print("Exit")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
