#program to check the given string is palindrome or not.

string = input("Enter a string to check whether it is palindrome or not: ")

if string [:: -1] == string[0 :]:
	print(string, "is a palindrome")
else:
	print(string,"is not a palindrome")
