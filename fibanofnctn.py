def fibano_recursive(a,b,num):
        if num<=0:
                return
        print(a)
        c=a+b
        a=b
        b=c
        fibano_recursive(a,b,num-1)
num=int(input("Enter the number of terms:"))
if num<=0:
        print("Please enter positive number")
else:
        print("Fibanocci series:")
        fibano_recursive(0,1,num)
