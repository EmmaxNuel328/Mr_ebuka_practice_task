def liter_petrol(prompt_liter,transaction = []):
	if prompt_liter >= 1 and prompt_liter <= 50:
		amount = 650 * prompt_liter
		return amount
	#return "Liters must be between 1-50!!!"


def amount_petrol(product,prompt_amount,transaction = []):
	if prompt_amount >= 650:
		liter = prompt_amount/650
		choice1 = f"""
``````````````````````````````````
 Customer Transaction receipt	
 Product:  {product}		
 Liter:   {liter: .2f}L		 
 Amount:      N{prompt_amount}	       
 Thank you for your patronage 	
_________________________________
"""
		transaction.append(choice1) 
		return choice1
	return "Amount must be above liter price!!!"


def liter_diesel(product,prompt_liter,transaction = []):
	if prompt_liter >= 1 and prompt_liter <= 50:
		amount = 720 * prompt_liter
		choice = f"""
``````````````````````````````````
WELCOME TO EMMAX FILLING STATION
 Customer Transaction receipt	
 Product:  {product}		
 Liter:   	{prompt_liter}L		 
 Amount:      N{amount}	       
 Thank you for your patronage 	
_________________________________
"""
		transaction.append(choice) 
		return choice
	return "Liters must be between 1-50!!!"

def amount_diesel(product,prompt_amount,transaction = []):
	if prompt_amount > 72:
		liter = prompt_amount/720
		transaction.append(f"Product: {product}, Liter: {liter}L, Amount: N{prompt_amount} ") 
		choice1 = f"""
``````````````````````````````````
 Customer Transaction receipt	
 Product:  {product}		
 Liter:   {liter:.2f}L	 
 Amount:      N{prompt_amount}	       
 Thank you for your patronage 	
_________________________________
"""
		transaction.append(choice1) 
		return choice1
	return "Amount must be above liter price!!!"




def liter_kerosene(product,prompt_liter,transaction = []):
	if prompt_liter >= 1 and prompt_liter <= 50:
		amount = 550 * prompt_liter
		choice = f"""
``````````````````````````````````
WELCOME TO EMMAX FILLING STATION
 Customer Transaction receipt	
 Product:  {product}		
 Liter:   	{prompt_liter}L		 
 Amount:      N{amount}	       
 Thank you for your patronage 	
_________________________________
"""
		transaction.append(choice) 
		return choice
	return "Liters must be between 1-50!!!"

def amount_kerosene(product,prompt_amount,transaction = []):
	if prompt_amount > 550:
		liter = prompt_amount/550
		transaction.append(f"Product: {product}, Liter: {liter}L, Amount: N{prompt_amount} ") 
		choice1 = f"""
``````````````````````````````````
 Customer Transaction receipt	
 Product:  {product}		
 Liter:   {liter}L		 
 Amount:      N{prompt_amount}	       
 Thank you for your patronage 	
_________________________________
"""
		transaction.append(choice1) 
		return choice1
	return "Amount must be above liter price!!!"  







		