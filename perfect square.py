num=int(input("Enter the number:"))

for i in range(1,num+1):
 if i*i==num:
     print("perfect square")
     break
 elif(i==num):
     print("Not perfect square")
