def is_prime(num):
        if num<=1:
                return False
        for i in range(2,int(num**0.5)+1):
                if num%i==0:
                        return False
        return True

n=int(input("Enter value of n to find nth prime number:"))
count=0
num=2
while count<n:
        if is_prime(num):
                count+=1
                if count==n:
                        print(f"The {n}th prime number is:{num}")
                        break
        num+=1

