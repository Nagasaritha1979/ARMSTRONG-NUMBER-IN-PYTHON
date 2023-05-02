# ARMSTRONG NUMBER


num=input("Enter a number")
order=len(num)

num1=int(num)

temp=num1

sum=0

while(num1):
    
    digit=num1 % 10
    sum=sum+pow(digit,order)
    num1=num1//10
    
if sum==temp:
    print(temp, " is an ARMSTRONG Number")
else:
    print(temp, " is not an ARMSTRONG Number")
