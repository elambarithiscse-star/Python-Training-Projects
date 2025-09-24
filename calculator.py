def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    while(b==0):
        print(a,"is not divisible by 0")
        c=int(input("again enter the value of B : "))
        b=c
    else:
        print(a/b)
loop=''
while(loop!='q'):
    
    a=int(input("Enter the value of A : " ))
    b=int(input("Enter the value of B : " ))
    choice = input("Enter your choice :addition (+) or subraction (-) or Multiplication (*) or division(/) ")

    if(choice=="+"):    #addition
        print(add(a,b))
    elif(choice=="-"):  #Subtraction
        print(sub(a,b))
    elif(choice=="*"):    #Multiplication
        print(mul(a,b))
    elif(choice=="/"):#division
        div(a,b)
    else:
        print("InValid Operator")
    
    loop=input("\ndo you want to quit or continue \nquit=q \ncontinue=c : ")

    