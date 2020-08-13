# Python Program to print table  
 
  
def table(n): 
    for i in range (1, 11):  
          
        # multiples from 1 to 10 
        print ("%d * %d = %d" % (n, i, n * i)) 
  
n =int(input( "number:"))
table(n) 
