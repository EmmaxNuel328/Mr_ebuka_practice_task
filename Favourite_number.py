favourite_number = 7
prompt = int(input('guess a number: '))
if prompt != 7:
	for prompt in range(prompt):
		print("Nice try, guess again!")	 
		prompt = int(input('guess a number: '))
if prompt ==7: 
	print("That's my favourite number!")	
