n=int(input("enter the number of rows:"))

for i in range(1,n+1,2):
  for s in range(i,n+1,2):
    print(" ",end="")
  for j in range(0,i):
    print("*",end="")
  print("\r")

for i in range(n-2,0,-2):
   for s in range(n+1,i,-2):
    print(" ",end="")
   for j in range(0,i):
      print("*",end="")
   print("\r")
