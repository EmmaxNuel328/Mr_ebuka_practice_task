# 1.
def access_third_element(numbers):
#for _ in numbers:
	third_element = numbers[2]
	return third_element

my_list = [1,2,46,4,5]
print("1. The third element is:",access_third_element(my_list),"\n")

#2.
def change_last_color(elements):
	elements[-1] = 'yellow'
	return elements

my_list = ['green','red','blue']
print("2. ",change_last_color(my_list),"\n")


#3 
def add_an_element(colors):
	new_color = 'purple'
	colors[-1] = 'yellow'
	colors.append(new_color)
	return colors

my_list = ['green','red','blue']
print("3. ",add_an_element(my_list),"\n")

#4
def remove_an_element(list):
	for index in list:
		index += 1
		list.remove(3)
		return list

my_list = [1,2,4,5,3]
print("4. ",remove_an_element(my_list),"\n")

#5
def  length_of_each_list(list):
	new_list = []
	index = 0
	for num in list:
		new_list.append(len(num))
	return new_list
my_list = ['EMMAX','EMMANUEL']
print("5. ",length_of_each_list(my_list),"\n")

		




#6
def sort_in_ascending_order(list):
	list.sort()
	return list

my_list = [1,4,2,4,5,6]
print("6. ", sort_in_ascending_order(my_list),"\n")	

#7.
def return_even_numbers(list):
	index = -1
	even_list = []
	for number in list:
		index += 1
		if list[index] % 2 == 0:
			even_list.append(list[index])
	return even_list
	

my_list = [1,2,4,5,3,2,6,8,10]
print("7.",return_even_numbers(my_list),"\n")

#8
def combine_two_list(list1,list2):
	list = list1 + list2
	return list

my_list1 = [1,2,0]
my_list2 = [3,4,2]

print("8. ",combine_two_list(my_list1,my_list2),"\n")


#9
def return_new_list(list):
	index = 0
	new_list = []
	for _ in list:
		if len(list[index]) >= 3:
			new_list.append(list[index])
		index += 1
	return new_list

my_list1 = ['yam','emmac','wert','wes','we','EMMAX','COLE PALMER','LIONEL MESSI']
print("9. ",return_new_list(my_list1,),"\n")


		
		
		