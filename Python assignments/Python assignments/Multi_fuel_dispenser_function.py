def liter_petrol(product,prompt_liter,transaction = []):
	if prompt_liter >= 1 and prompt_liter <= 50:
		amount = 650 * prompt_liter
	else:
		print("Liters must be between 1 - 50!!!")
	transaction.append(f"Product: {product}, Liter: {prompt_liter}L, Amount: N{amount} ") 
	return transaction
		