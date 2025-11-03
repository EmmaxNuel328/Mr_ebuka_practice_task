numbers = int(input('Enter a five digits(in binary):'))
number1 = numbers//10000
number2 = (numbers%10000)//1000
number3 = (numbers%10000%1000)//100
number4 = (numbers%10000%1000%100)//10
number5 = (numbers%10000%1000%100)%10
print(number1,number2,number3,number4,number5)
decimal = int(number1*16)+int(number2*8)+int(number3*4)+int(number4*2)+int(number5*1)
print(decimal)