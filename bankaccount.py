class Bankaccount:  
    def __init__(self, account_number, account_holder,balance):
        self. account_number = account_number # Public
        self._account_holder = account_holder # Protected
        self.__balance = balance # Private

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    
    def withdraw(self,amount):        
        if 0 < amount <= self.__balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def Balance(self):
        print(f"Your Balance is : {balance} ")
        


    
    def _display_holder_info(self):
        print(f"Account Holder: {self._account_holder}")

    
    def __apply_bank_charges(self):
        self.__balance -= 50
        print("₹50 bank charge applied.")

    def month_end_process(self):
        print("Month-end processing done.")


acc=int(input("Enter your account number : "))
name=input("Enter your name : ")
bal=1000
balance=bal
account = Bankaccount(acc,name,bal)
while True:
    option =int(input("Enter your choice 1.deposit 2.Withdraw 3.Balance \n :"))
    if(option==1):
        amount = int(input("Enter the amount you want to deposit :"))
        account.deposit(amount)
    elif(option==2):
        amount=int(input("Enter the amount you want to withdraw : "))
        account.withdraw(amount)
    elif(option==3):
        account.Balance()
    else:
        print("Enter a Valid option")
        
    a=input("Do you want continue  yes[y] or no[n] \n: ")
    if(a=="y"):
     continue
    else:
        break
                

           
            
