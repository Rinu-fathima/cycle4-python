def add(a,b):
        return a+b

def sub(a,b):
        return a-b

def mul(a,b):
        return a*b

def div(a,b):
        if b!=0:
                return a/b
        else:
                return "Error !Division by zero"

a=float(input("Enter number 1:"))
b=float(input("Enter number 2:"))
while True:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        choice=input("Enter Choice")
        if choice=='5':
                print("Exiting the calculator")
                break
        if choice in['1','2','3','4']:
                if choice=='1':
                        print(f" {a}+{b}={add(a,b)}")
                elif choice=='2':
                        print(f" {a}-{b}={sub(a,b)}")
                elif choice=='3':
                        print(f" {a}*{b}={mul(a,b)}")
                elif choice=='4':
                        print(f" {a}+{b}={div(a,b)}")
        else:
                print("Invalid choice!Ty Again")
