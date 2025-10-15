def deposit(amount,account_balance,transaction = []): 
	account_balance += amount
	return account_balance
def withdraw(amount,account_balance,transaction = []):
	account_balance -= amount
	return account_balance
balance = 0
transaction = []
Menu = """ 
1. Deposit
2. Withdraw
3. Transaction history
0. Back
""";
print(Menu)
prompt = -1
while prompt != "0" :
	prompt = input("Enter from the above menu: ")
	match(prompt): 
		case "1" :
			deposit_amount = float(input("Enter amount to deposit: "))
			balance = deposit(deposit_amount,balance)
			print("N",balance)
			transaction.append(f"Deposited: N{deposit_amount}| New Balance: N{balance}")
			print(transaction)
		case "2" :
			withdraw_amount = float(input("Enter amount to withdraw: "))
			balance = withdraw(withdraw_amount,balance)
			print(balance)
		case "0" : print("Thank yoy for using Transaction Log App")
			


		case _: print("INVALID","\t",Menu)