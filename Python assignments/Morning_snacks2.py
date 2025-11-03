number1 = int(input('Enter an integer'))
number2 = int(input('Enter an integer'))
number3 = int(input('Enter an integer'))

second_largest =number4
if number1 > number2 and number1 < number3:
	second_largest = number1
if number2 > number1 and number2 < number3:
	second_largest = number2
if number3 > number2 and number3 < number3:
	second_largest = number3
print(second_largest)
    