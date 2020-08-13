#default arguments
def printinfo( name, age = 35 ):  
	print( "Name: ", name) 
	print ("Age ", age) 
	return; 
printinfo( age=50, name="miki" ); 
printinfo( name="miki" );
