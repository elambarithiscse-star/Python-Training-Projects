import random
secret_number = random.randint(1,10)
attempt=3
while (attempt>=1):
    guess=int(input("Guess the number between 1 to 10 : "))
    if(guess==secret_number):
        print("You Guessed the correct Number!!")
    elif(guess<secret_number):
        print("This number is low")
    elif(guess>secret_number):
        print("This number is High")
    attempt-=1
    if(attempt==0):
        print("You ran out of attempts!!")
    else:
        print(f"You have {attempt} attempts left!"except attempt==0)
    if(attempt==0 or guess==secret_number):
        a=input("Do you want to Continue(C) or Exit(E) : ")
        if(a=='c'):
            attempt=3
        else:
            break
    
    
    
        
    