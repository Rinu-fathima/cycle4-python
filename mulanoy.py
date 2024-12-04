t=int(input("Enter no of terms:"))
terms_lst=[]
for i in range(t):
        terms=int(input("Enter  terms:"))
        terms_lst.append(terms)
multiplefnctn=filter(lambda x:x%3==0,terms_lst)
print("Multiples of 3 are:")
multiple_fnctn_list=list(multiplefnctn)
print(multiple_fnctn_list)
