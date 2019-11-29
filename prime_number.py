#This Program is to check whether number is prime or not 

Number = int(input("Enter the number to check it's prime number or not: "))

for i in range(2, Number):
	if Number % i == 0:
		print("Not an Prime Number")
	break
else:
	print("It's an Prime Number")