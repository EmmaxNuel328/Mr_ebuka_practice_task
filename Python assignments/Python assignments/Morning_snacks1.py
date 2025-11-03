first = input('Enter First score:')
second = input('Enter Second score:')
third = input('Enter Third score:')


largest = first
if third > largest:
	largest = third
if second > largest:
	largest = second
print('Largest', '=', largest)
