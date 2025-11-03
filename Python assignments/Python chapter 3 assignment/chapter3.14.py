pi = 3

for counter in range (3, 11):
	while counter > 3:
		counter = counter * (counter - 1)
		break
	pi = pi - ( pi / counter)
	

print(pi)
