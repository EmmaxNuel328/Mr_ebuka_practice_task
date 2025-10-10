my_list = [1,2,3,4,34,6,7]
index = -1
sum = 0
largest = my_list[0]
for numbers in my_list:
	index += 1
	if(my_list[1] > largest):
		largest = my_list[1]
	if(my_list[2] > largest):
		largest = my_list[2]  
	if(my_list[3] > largest):
		largest = my_list[3]
	if(my_list[4] > largest):
		largest = my_list[4]
	if(my_list[5] > largest):
		largest = my_list[5] 
	if(my_list[6] > largest):
		largest = my_list[6] 		
print(largest)