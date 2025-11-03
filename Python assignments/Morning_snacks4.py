number1 = int(input('Enter first number:'))
number2 = int(input('Enter second number:'))
number3 = int(input('Enter third number:'))
number4= int(input('Enter fourth number:'))

sum = int(number1 + number2 + number3 + number4)
print('sum', '=', sum)

smallest = number1
largest = number1

if number2 < smallest:
	smallest = number2
if number3 < smallest:
	smallest = number3
if number4 < smallest:
	smallest = number4
print(smallest)
second_largest = number1
if number2 > smallest and number2 < largest:
	second_largest = number2
if number3 > smallest and number3 < largest:
	second_largest = number3
if number4 > smallest and number4< largest:
	second_largest = number4
print(second_largest)
third_largest = number1
if number2 > smallest and number2 < second_largest:
	third_largest = number2
if number3 > smallest and number3 < second_largest:
	third_largest = number3
if number4 > smallest and number4 < second_largest:
	third_largest = number4
print(third_largest)
if number2 > largest:
	largest = number2
if number3 > largest:
	largest = number3
if number4 > largest:
	largest = number4
print(largest)


 









