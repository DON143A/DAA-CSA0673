s=int(input("Enter the size of array:"))
a=[]
for i in range(s):
      n=int(input(f'Element {i+1}:'))
      a.append(n)
      
print(max(a))
