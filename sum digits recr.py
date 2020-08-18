sum=0
def sum_digits(num):
    global sum
    if(num>0):
        rem=num%10
        sum=sum+rem
        sum_digits(num//10)
    return sum

num=int(input("Enter any number:"))
sum=sum_digits(num)
print("Sum of digits of given number :",sum)
        
