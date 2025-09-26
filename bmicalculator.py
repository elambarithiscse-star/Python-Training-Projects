print("Welcome to BMI calculator")
height=int(input("Enter your Height(in cms) : "))
weight=int(input("Enter your Weight : "))
def calc():
    meters=height/100
    bm=(weight/meters**2)
    bm1=float(format(bm,".1f"))
    #print("Your BMI value is :",bm1)
    return bm1
def check():
    bmi=calc()
    if(bmi<=18.4):
        print("You are underweight,and your bmi is",bmi)
    elif(bmi>=18.5 and bmi<=24.9):
        print("You are Normal Weight,and your bmi is",bmi)
    elif(bmi>=25 and bmi<=39.9):
        print("you are overweight,and your bmi is",bmi)
    elif(bmi>=40):
        print("you are obese,and your bmi is",bmi)
    else:
        print("Invalid")
check()