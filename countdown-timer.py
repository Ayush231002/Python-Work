import time 

# define the countdown fun. 
def countdown(a): 
	
	while a: 
		mins, secs = divmod(a, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		a -= 1
	
	print('Fire in the hole!!') 


# input time in seconds 
a = input("Enter the time in seconds: ") 

# function call 
countdown(int(a)) 
