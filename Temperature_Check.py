prompt = int(input("Enter Temperature: "))
if prompt > 30:
	print("Hot!")
elif prompt >= 15 and prompt <= 30:
	print("Nice!")
elif prompt < 15:
	print("Cold!")