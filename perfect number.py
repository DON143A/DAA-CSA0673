num=int(input("Enter the number:"))
s=0
for i in range(1,num):
        if num%i == 0 :
            s+=i
else:
    if num==s:
        print("perfect number")
    else:
        print("Not a perfect number")
        
