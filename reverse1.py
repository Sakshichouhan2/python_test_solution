def ReverseWord(Input):

	String = input.split(" ")
	#it will split the given string 

	String = String[-1::-1] 
	#it will reverse the given string
	
	output = ' '.join(String)
	#join mathod will join the splitted string 
	
	return output 

if __name__ == "__main__": #main is a method 
	input = 'my name is michele'
print(input)
print (ReverseWord(input)) 
