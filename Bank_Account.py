class BankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance

    def deposit(self,amount):
        print(f"Rs.{amount} is added in your acccount")
        self.balance+=amount
        
        

    def withdraw(self,amount):
        if self.balance>=amount:
            print(f"Rs.{amount} is withdraw from your acccount")
            self.balance-=amount
        else:
            print("Insuffcient fund")
        

    def display(self):
        print(f"Account holder: {self.acc_holder}")
        print(f"Current Balance: {self.balance}")
        print("Welcome to Shadow National Bank")

name=input("Enter Name")
balance=float(input("Enter initial balance"))
account=BankAccount(name,balance)

while True:
    print("1.Deposite")
    print("2.Withdraw")
    print("3.Display")
    print("4.exit")    

    choice=input("Enter your choice")

    if choice=="1":
        amt=float(input("Enter amount to deposit"))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == "3":
        account.display()
    elif choice == "4":
        print("Thank you! Visit again.")
        break
    else:
        print("Invalid choice. Try again.")



