def rev(num,r=0):
    if num == 0:
        return r
    else:
        return rev(num//10,r*10+num%10)
num=int(input("Enter the number"))
re=rev(num)
print("reversed number:",re)
