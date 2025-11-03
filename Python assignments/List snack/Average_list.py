my_list = [1,2,3,4,5,6,7]
index = -1
sum = 0
for numbers in my_list:
	index += 1
	sum += my_list[index]
	average = sum/len(my_list)
	print(my_list[index])
print("Average : ", average)