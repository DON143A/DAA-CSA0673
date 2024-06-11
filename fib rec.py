def fib(n,first,second):
  if n>2:
    third=first+second
    print(',',third,end="")
    first=second
    second=third
    return fib(n-1,first,second)
n=int(input("Enter No.of terms requried:"))
if n<=0:
      print("Invalid input")
elif n==1:
      print("0")
elif n==2:
      print("0,1")
else:
      print("0,1",end="")
      fib(n,0,1)
