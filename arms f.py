#amstrong using functions
num = int(input("Enter a number: "))
def find(num):
    sum = 0  
    x = num  
    while x > 0:  
       digit = x % 10  
       sum += digit ** 3  
       x //= 10  
    if num == sum:  
       print(num,"is an Armstrong number")  
    else:  
       print(num,"is not an Armstrong number")
find(num);
