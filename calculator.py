# A simple calculator

print("simple calculator")

def addition(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y

print("Enter 1 for addition")
print("Enter 2 for substraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

num1=float(input("enter first number"))
num2=float(input("enter second number"))
choice=int(input("Enter your choice what you have to perform"))

if choice==1:
    print(f"sum= {addition(num1,num2)}")
elif choice==2:
    print(f"difference= {substract(num1,num2)}")
elif choice==3:
    print(f"product= {multiply(num1,num2)}")
elif choice==4:
    print(f"quotient= {divide(num1,num2)}")
else:
    print("invalid")