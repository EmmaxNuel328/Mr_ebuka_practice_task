my_list = [1,2,3,4,5,6,7]
index = -1
sum = 1
for numbers in my_list:
	index += 1
	if(index % 3 == 0):
		sum *= my_list[index]
		print(my_list[index])
print("Sum of numbers at every third position: ", sum)