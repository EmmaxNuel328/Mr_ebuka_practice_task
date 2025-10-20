from Multi_fuel_dispenser_function import *
available_petroleum = """
1. petrol = 650/liter
2. Diesel = 720/liter
3. Kerosene = 550/liter
4. Gas = 480/liter
"""
print(available_petroleum)
index = 0
transaction = []
prompt = 2
while prompt != "0":
	prompt = input("Enter type of fuel you want to buy:  ")
	collect = input("liter or amount: ")
	match prompt:
		case "1": 
			if collect == "liter":
				prompt_petrol = int(input("How many liters of petrol are you buying (650/liter): "))
				print(liter_petrol("petrol",prompt_petrol))
				
			