n=int(input("Enter number of rows:"))
nums=[]
for i in range(1,n+1):
   c=1
   row=[]
   for j in range(1,i+1):
     row.append(c)
     c=int(c*(i-j)/j)
   nums.append(row)
print(nums)

