secret = 8
for prompt in "prompt": 
	prompt = int(input("Enter a number: "))
	if prompt == secret:
		print("Correct!")
		break
	else:
		print("Try again")