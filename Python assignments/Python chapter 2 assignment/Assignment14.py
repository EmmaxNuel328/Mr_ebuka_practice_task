# COllect age from user
# initialize max heart rate to be equal to 220 - age
# print the max heart rate 
# check if max heart rate is less or equal to 200 and greater than 190 ;
# display target heart rate, 
# if not check if max heart rate is less or equal to 190 and greater than185;
# if not check if max heart rate is less or equal to 185 and greater than 180;
# if not check if max heart rate is less or equal to 180 and greater than 
175;
# if not check if max heart rate is less or equal to 175 and greater than 
170 
# if not 


age = int(input('Enter your age'))
maxheartrate = 220 - age
print('max heart rate', '=', (maxheartrate),'bpm')
if maxheartrate <= 200  and maxheartrate > 190:
	print('Target heart rate', '=', '100 - 170','bpm' )
if maxheartrate <= 190 and maxheartrate > 185:
	print('Target heart rate', '=', '95 - 162','bpm')
if maxheartrate <= 185 and maxheartrate > 180:
	print('Target heart rate', '=', '93 - 157','bpm')
if maxheartrate <= 180 and maxheartrate > 175:
	print('Target heart rate', '=', '90 - 153','bpm')
if maxheartrate <= 175 and maxheartrate > 170:
	print('Target heart rate', '=', '88 - 149','bpm')
if maxheartrate <= 170 and maxheartrate > 165:
	print('Target heart rate', '=', '85 - 145','bpm')
if maxheartrate <= 165 and maxheartrate > 160:
	print('Target heart rate', '=', '83 - 140','bpm')
if maxheartrate <= 160 and maxheartrate > 155:
	print('Target heart rate', '=', '80 - 136','bpm')
if maxheartrate <= 155 and maxheartrate > 150:
	print('Target heart rate', '=', '78 - 132','bpm')
if maxheartrate <= 150:
	print('Target heart rate', '=', '75 - 128','bpm')




