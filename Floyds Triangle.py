n=int(input("Enter number of rows:"))
c=1
for i in range(1,n+1):
   for j in range(1,i+1):
      print(c," ",end="")
      c=c+1
   print("\r")
