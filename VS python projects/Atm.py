print("Welcome to ATM ")
class ATM:
    def __init__(self,pin,balance):
        self.__pin = pin
        self.__balance=balance

    def deposit(self,amount):  
        if amount>0:
            self.__balance+=amount
            print(f"The amount you deposited,{amount}, New balance is {self.__balance} ")
        else:
            print("Enter a valid amount")
    
    def withdraw(self,amount):
        if amount>0:
            self.__balance-=amount
            print(f"The amount you withdrew, {amount}, New balance is {self.__balance}" )
        else:
            print("Enter the valid amount")

    def Balance(self):
        print(f"Your balance is {self.__balance}")


balance=1000
bal=balance
Pass=1234
password=Pass
inp=ATM(password,bal)


#ATM.deposit(amt)
#ATM.withdraw(amt)
while True:
    pas=int(input("Enter your Pin : "))
    if(pas== password):
        option=int(input("Enter the option  1.deposit | 2.Withdraw | 3. check Balance \n :")) 
        if(option==1):
            amount=int(input("Enter the Amount you want to deposit : "))
            inp.deposit(amount)
        elif(option==2):
            amount=int(input("Enter the amount you want to withdraw : "))
            inp.withdraw(amount)
        elif(option==3):
            inp.Balance()
        else:
            print("Enter a valid option ")
    else:
        print("Incorrect pin , Enter the Correct pin")
        continue

    decide=input("Do you want to continue yes[y] no[n] : ")
    if(decide=='n'):
        break
    else:
        continue


