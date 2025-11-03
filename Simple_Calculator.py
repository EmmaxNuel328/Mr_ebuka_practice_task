prompt1 =int(input( "Enter first number: "))
prompt2 =  int(input("Enter second number: "))
prompt3 = input("Enter Add,subtract,multiply,divide:")
sum = "add"
difference = "subtract"
product = "multiply"
division = "divide"
def add(prompt1,prompt2):
	return prompt1 + prompt2
def subtract(prompt1,prompt2): 
	return prompt1 - prompt2
def multiply(prompt1,prompt2):
	return prompt1 * prompt2
def divide(prompt1,prompt2):
	return prompt1/prompt2
if prompt3 == sum:
	print(add(prompt1,prompt2))
elif prompt3 == difference:	
	print(subtract(prompt1,prompt2))
elif prompt3 == product:	
	print(multiply(prompt1,prompt2))
elif prompt3 == division:	
	print(divide(prompt1,prompt2))
elif prompt3 == product:	
	print(multiply(prompt1,prompt2))
elif prompt3!=sum or prompt3!=difference or prompt3!=division or prompt3!=power:
	print("INVALID INPUT!")
