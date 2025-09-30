password = 'secret123'
prompt = input('Enter PASSWORD: ')
if prompt == password:
	print('Access granted! Welcome')
if prompt != password:
	print('Access denied!')