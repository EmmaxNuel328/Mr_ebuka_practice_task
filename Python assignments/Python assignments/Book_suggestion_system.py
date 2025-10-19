from Book_suggestion_function import *
book_suggestion_system = """
	|``````````````````````|
	|    EMMAX LIBRARY     |
	|``````````````````````|
	|   1. Get Book        |
	|   2. Add Book        |
	|   3. Remove Book     |
	|   4. Update Book     |
	|   5. Show all books  |
	|   0. BACK            |
	|______________________|
"""
print(welcome_page())
collect = input("Enter 1 to go to option: ")
book_list = ["living in Eko" ,"Without a silver spoon" ,"Naruto","Supa strika","DC comics",'Emmax',"One piece","Intro to Python","Intro to Javascript","Dragon balls","Attack on titans","The Flash","Blue lock","Avengers"]
index = 0
prompt = 1
stored_books = []
while prompt != "0":
	print(book_suggestion_system)
	prompt = input("Enter a choice from the above: ")
	match(prompt):
		case "1":
			print(suggest_book(book_list))
			prompt_suggest = "yes"
			while prompt_suggest != "no":
				prompt_suggest = input("Do you another suggestion(yes/no): ")
			
				if prompt_suggest == "yes":
					print(suggest_book(book_list))
		case "2":
			prompt_add = input("Enter name of book you want to add: ")
			print(add_books(prompt_add,book_list),"\n",prompt_add,"Added successfully")

			
		
				
		case "3": 
			prompt_remove = input("Enter name of book you want to  remove:")
			print(remove_books(prompt_remove,book_list),"\n",prompt_remove,"Removed successfully")
		case "4":
			old_name = input("Enter old title: ")
			new_name = input("Enter new title: ")
			print(update_books(old_name,new_name,book_list))
		case "5":
			print(show_books(book_list))
		case "0":
			print(back())
		case _ :
			print("INVALID INPUT!")
			
		
				