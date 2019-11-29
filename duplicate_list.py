#This program will check and print all dublicate elements in your list and append it in a new list

def remove(duplicate):
	list = [] 
	for number in duplicate: 
		if number not in list: 
			list.append(number) 
	return list 
	
# Driver Code 
duplicate = [8, 4, 12, 20, 5, 12, 20, 7, 2, 4] 
#It will only print a unique number will not print any duplicate number
print(remove(duplicate)) 


