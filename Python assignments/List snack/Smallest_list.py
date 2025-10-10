my_list = [-1,2,3,4,34,-56,7]
index = -1
sum = 0
smallest = my_list[0]
for numbers in my_list:
	index += 1
	if(my_list[1] < smallest):
		smallest = my_list[1]
	if(my_list[2] < smallest):
		smallest = my_list[2]  
	if(my_list[3] < smallest):
		smallest = my_list[3]
	if(my_list[4] < smallest):
		smallest = my_list[4]
	if(my_list[5] < smallest):
		smallest = my_list[5] 
	if(my_list[6] < smallest):
		smallest = my_list[6] 		
print(smallest)