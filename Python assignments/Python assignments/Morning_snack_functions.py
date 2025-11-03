from functools import reduce
my_list = [1,2,3,4,5]
def get_square(prompts):
	return prompts ** 2
numbers = list(map(get_square,my_list))
print("1.",my_list)
print("  ",numbers,"\n")


my_fruits = ["apple","banana","kiwi","pineapple"]
def get_length(prompts):
	return len(prompts)
length = list(map(get_length,my_fruits))
print("2.",my_fruits)
print("  ", length,"\n")

my_numbers = [2,4,3,5,6,8,10,18]
def is_even(prompts):
	return prompts % 2 == 0
even = list(filter(is_even,my_numbers))
print("3.",my_numbers)
print("  ", even,"\n")


collection = ["apple","banana","pineapple","kiwi"]
def is_length_above_five(prompts):
	return len(prompts) >= 5 
collections = list(filter(is_length_above_five,collection))
print("4.", collection)
print("  ", collections,"\n")

words = ["I","love","python","snacks"]
def concatenate(strings,space):
	return strings + "-" + space
sentence = reduce(concatenate,words)
print("5.", words)
print("  ", sentence)