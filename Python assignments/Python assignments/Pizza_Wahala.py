menu = """
	ORDER WHAT YOU CAN AFFORD
|``````````````````````````````````````````````````````````|
|  PIZZA TYPE       | 	NUMBER OF SLICES | PRICE PER BOX   |	
|``````````````````````````````````````````````````````````|
| SAPA              |	4		 | 2,500           |
|``````````````````````````````````````````````````````````|
| SMALL MONEY       |   6                | 2,900           |
|``````````````````````````````````````````````````````````|
|BIG BOYS           |   8                | 4,000           |
|``````````````````````````````````````````````````````````|
|ODOGWU             |   12               | 5,200           |
````````````````````````````````````````````````````````````
"""
print(menu)
pizza_Type =input("pizza type: ")

match pizza_Type:
	case "sapa":
		guest = int(input("Enter number of guest: "))
		slices = 4
		box = guest/slices
		price = box * 2500
		remainder = 0
		
		if guest % slices :
			box = box + 1
			slices = slices * box
			remainder = guest - slices
			print("Number of box(es)", box)