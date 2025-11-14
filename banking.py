print("please enter your name:- ")
name=input("your name:-")
print("welcome",name,"to bank")


def show_balance():
    
    print("----------------")
    print(f"your balance is :- {balance}")
    
def deposit():
    
    amount=float(input("enter your amount:-"))
    if amount<0:
        print("invalid input")
    else:
        return amount

def withdraw():
    
    amount=float(input("enter your amount:-"))
    if balance < amount:
        print("insufficient balance")
        return 0
    elif amount < 0:
        print("invalid input")
        return 0
    else:
        return amount

balance=0
is_running=True
while is_running:
 print("banking:-")
 print("press 1 to show your balance")
 print("press 2 to show your deposit")
 print("press 3 to show your withdraw")
 print("enter 4 to exit")

    
 choice=input("enter your choice")
 if choice=='1':
     show_balance()
 elif choice=='2':
     balance+=deposit()
 elif choice=='3':
     balance-=withdraw()
 elif choice=='4':
     is_running=False
     print("thankx for banking with us")
 else:
     print("invalid input")