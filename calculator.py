num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice:")
if choice==1:
result=num1+num2
print("Addition=",result)
elif choice==2:
result=num1-num2
print("Subtraction=",result)
elif choice==3:
result=num*num2
print("Multiplication=",result)
elif choice==4:
result=num/num2
print("Division=",result)
else:
print("Invalid choice")
