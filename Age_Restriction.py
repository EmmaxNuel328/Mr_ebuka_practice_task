minimum_age = 10
prompt = int(input("Enter your age: "))
if prompt >= minimum_age:
	print("Welcome to the show!")
elif prompt < 0:
	print("invalid Age! Are you ALIEN!")
elif prompt < 10:
	print("Sorry, you're to young!")
