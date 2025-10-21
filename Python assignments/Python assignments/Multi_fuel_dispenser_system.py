from Multi_fuel_dispenser_function import *
dashboard = """
WELCOME TO EMMAX FILLING STATION

1. Buy petroleum
2. Show transaction history
"""
print(dashboard)
prompt_dashboard = input("Enter operation: ")
available_petroleum = """
WELCOME TO EMMAX FILLING STATION
1. petrol = 650/liter
2. Diesel = 720/liter
3. Kerosene = 550/liter
4. Gas = 480/liter
"""
if prompt_dashboard == "1":
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
					customer_transaction_receipt = liter_petrol("petrol",prompt_petrol)
					print(customer_transaction_receipt  )
					index += 1
				if collect == "amount":
					prompt_petrol1 = int(input("How much petrol are you buying (650/liter): "))
					print(amount_petrol("petrol",prompt_petrol1))
				else:
					print("INVALID INPUT!!!")
			case "2":
				if collect == "liter":
					prompt_diesel = int(input("How many liters of diesel are you buying (720/liter): "))
					customer_transaction_receipt = liter_diesel("diesel",prompt_diesel)
					print(customer_transaction_receipt  )
				if collect == "amount":
					prompt_diesel1 = int(input("How much diesel are you buying (720/liter): "))
					print(amount_petrol("diesel",prompt_diesel1))
				else:
					print("INVALID INPUT!!!")
			case "3": 
				if collect == "liter":
					prompt_kerosene = int(input("How many liters of kerosene are you buying (550/liter): "))
					customer_transaction_receipt = liter_kerosene("kerosene",prompt_kerosene)
					print(customer_transaction_receipt  )
				if collect == "amount":
					prompt_kerosene1 = int(input("How much kerosene are you buying (550/liter): "))
					print(amount_kerosene("kerosene",prompt_kerosene1))
				else:
					print("INVALID INPUT!!!")


					

				
			
				
			