print("\n=== To-Do List ===")
while True:
    choice=int(input("Enter your choice : "))
    if(choice==2):     #add task    
        Add=list(input("Enter your seprated by space: ").split())
    elif(choice==1):        #view
        print(Add)
            
    elif(choice==3):  #delete task
        rem=input("Enter the task you want to remove : ")
        Add.remove(rem)
            
    elif(choice==4):  #exit
        break
            
    else:
        print("Enter a valid choice")
            
    a=input("do have any other choice ? yes(y) no(n) : ")
    if(a=='n'):
        break
        
        
    
    