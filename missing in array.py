arr=[1,2,3,4,6]
l=len(arr)
i=0
while i!=l-1:
  if arr[i+1]==arr[i]+1 :
      i=i+1
      continue
  else:
        print("missing number=",arr[i]+1)
        break

if(i==l-1):
  print("nothng missing")
