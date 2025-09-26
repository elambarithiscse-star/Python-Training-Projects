print("Welcome to ATM Machine")
Pass=1234
while True:
    password=int(input("Enter Your Password : "))
    if(password==Pass):
        print("Correct Password!! \n1.Debit \n2.Withdrawal \n3.Check Balance")
        break
    else:
        print("Incorrect Password !!")
        print("")