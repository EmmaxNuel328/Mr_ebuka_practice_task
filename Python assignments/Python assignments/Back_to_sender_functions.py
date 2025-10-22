def get_wage(prompt):
	if prompt >= 0 and prompt < 50:
		wage = (prompt * 160) + 5000
	if prompt >= 50 and prompt < 60:
		wage = (prompt * 200) + 5000
	if prompt >= 60 and prompt < 70:
		wage = (prompt * 250) + 5000
	if prompt >= 70:
		wage = (prompt * 500) + 5000
	if type(prompt) == str:
		raise TypeError ("INVALID INPUT")
	return wage 
	
	