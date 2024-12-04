def add_num(*args):
        """This function used as an example of variable-length arguments"""
        total=0
        for num in args:
                total+=num
        return total
number_list=[]
n=int(input("Enter numbers in list:"))
for i in range(n):
        num=int(input("Enter a number:"))
        number_list.append(num)
result=add_num(*number_list)
print(f"Sum={result}")
