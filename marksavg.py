Student_name = (input("Enter name: "))
age = int(input("Enter age: "))
sub1 = int(input("Enter sub1 mark: "))
sub2 = int(input("Enter sub2 mark: "))
sub3 = int(input("Enter sub3 mark: "))
print("Name : ",Student_name)
print("Age : ",age)
total = sub1+sub2+sub3
print("Total : ",total)
avg = total//3
print("Avg : ",avg)
if(avg>=85 and avg<=100):
    print("Passed with first Class")
elif(avg>=65 and avg<=84):
    print("Passed with second Class")
elif(avg>=50 and avg<=64):
    print("Passed with Third Class")
elif(avg<50):
    print("Fail!!")
else:
    print("Invalid marks")
    
                