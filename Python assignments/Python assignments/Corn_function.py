collect = input("Enter a word: ")
def get_first_and_last2_character(prompt):
	my_list = []
	index = 0
	for letters in prompt:
		my_list.append(letters)
	for index in range(len(collect)):
		if len(prompt) > 2:
			return my_list[0] + my_list[1] + my_list[-2] + my_list[-1] 
		if len(prompt) < 2:
			return []
		if len(prompt) == 2:
			return prompt * 2
print(get_first_and_last2_character(collect))



collect1 = input("Enter a word: ")
def add_ing_at_end(prompt):
	my_list = []
	index = 0
	for letters in prompt:
		my_list.append(letters)
	if my_list[-1] == "g" and my_list[-2] == "n" and my_list[-3] == "i" :
		return prompt + "ly"
	for index in range(len(prompt)):
		if len(prompt) >= 3:
			return prompt + "ing"
		if len(prompt) < 3:
			return prompt
			
	
print(add_ing_at_end(collect1)) 


my_list = []
index = 0
for _ in range(0,6):
	index += 1
	collect2 = input("Enter a word: ")
	my_list.append(collect2)
	
print(my_list)

def longest_and_length_of_the_longest_word(prompt):
	index = 0
	#for index in range(len(prompt)):
		
	#return my_list

#print(longest_and_length_of_the_longest_word(collect2)) 


#collect8 = input('Enter a word: ')

def take_and_remove_characters_with_odd_index(prompt):
	my_list = []
	for letter in range(len(prompt)):
			my_list.append(letter)
			#if letter % 2 != 0:
			return my_list[letter]
				
				
#print(take_and_remove_characters_with_odd_index(collect8))



def return_minimum_number(prompt):
	minimum = prompt[0]
	count = 0
	for _ in prompt:
		if prompt[count] < minimum:
			minimum = prompt[count]
		count += 1
	return minimum
my_list = [4,4,3,5,5, -100,555]
print(return_minimum_number(my_list))
	


def return_maximum_number(prompt):
	maximum = prompt[0]
	count = 0
	for _ in prompt:
		if prompt[count] > maximum:
			maximum = prompt[count]
		count += 1
	return maximum
my_list = [4,4,3,5,5, -100,555]
print(return_maximum_number(my_list))
	


