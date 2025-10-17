def deposit(amount,account_balance,transaction = []): 
	account_balance += amount
	transaction.append(f"Deposited: N{amount}| New Balance: N{account_balance}")

	return account_balance
def withdraw(amount,account_balance,transaction = []):
	if amount > account_balance:
		return "INSUFFICIENT FUND"
	account_balance -= amount
	return account_balance
#def show_transactions(transaction = []):
#	transaction.append(f"Deposited: N{amount}| New Balance: #N{account_balance}","\t")
#	return transaction
