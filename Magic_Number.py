magic_number = 42
for prompt in "prompt":
	prompt = input("Enter a number: ")
	if prompt == "42":
		print("You found the magic number")
		break
	elif prompt != "42": 
		print("Keep looking!")
		