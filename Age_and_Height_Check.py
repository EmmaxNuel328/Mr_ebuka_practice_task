age =int(input('Enter your Age: '))
height =int(input('Enter your Height: '))
if age >= 12 and height >= 140:
		print("Ride allowed!")
if age >= 12 and height < 140:
		print("Too short")
if age < 12 and height >= 140:
	print("Too young")
if age < 12 and height < 140:
	print("Too young and Too short")

