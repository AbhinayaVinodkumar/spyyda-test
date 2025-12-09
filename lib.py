lib={}
def add_book():
	book_id = input("Enter book id:")
	if book_id in lib:
		print("book id already exists\n")
		return
	title=input("Enter book title:")
	author=input("ENter author name:")
	lib[book_id]={
		"title":title,
		"author":author,
		"status":"Available"
	}
	print("Book added successfully\n")
def search_book():
	book_id = input("Enter book id to search:")
	if book_id in library:
        book = library[book_id]
        print(f"\nBook Found:")
        print(f"ID: {book_id}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Status: {book['status']}\n")
    else:
        print("Book not found!\n")
def borrow_book():
	book_id = input("Enter Book ID to borrow: ")
 	if book_id not in library:
        	print("Book not found!\n")
        	return
	if library[book_id]["status"] == "Borrowed":
        	print("Book is already borrowed!\n")
    	else:
        	library[book_id]["status"] = "Borrowed"
        	print("Book borrowed successfully!\n")
def return_book():
	book_id = input("Enter Book ID to return: ")
	if book_id not in library:
        	print("Book not found!\n")
        	return
	if library[book_id]["status"] == "Available":
		print("Book is not borrowed.\n")
	else:
		library[book_id]["status"] = "Available"
		print("Book returned successfully!\n")
def menu():
	while True:
		print("===== Library Management System =====")
        	print("1. Add Book")
        	print("2. Search Book")
        	print("3. Borrow Book")
        	print("4. Return Book")
        	print("5. Exit")
		choice = input("Enter your choice: ")
		if choice == "1":
            		add_book()
        	elif choice == "2":
            		search_book()
        	elif choice == "3":
            		borrow_book()
        	elif choice == "4":
            		return_book()
        	elif choice == "5":
            		print("Exiting Program...")
            		break
        	else:
            		print("Invalid Choice! Try again.\n")
men()
How to run a code?
Save your code in a file lib.py
Open Command Prompt / Terminal
Run: python program.py

logical explantion
The program is built using simple Python functions and a dictionary to perform basic library operations. All book details are stored in a dictionary called library, where each book has a unique book_id used as the key. The value for each key is another dictionary containing the book’s title, author, and status. This structure makes it easy to access and update information quickly.

The program provides four main functions: add, search, borrow, and return. When adding a book, the user enters the ID, title, and author. The program checks if the ID already exists to prevent duplicates. The search function simply checks if the entered ID is present and displays its details. Borrowing a book works by checking its availability; if the book is not already borrowed, the status is updated to “Borrowed”. Returning a book reverses this process by setting the status back to “Available”.

All these operations are controlled by a console menu, which runs inside an infinite loop. The user selects an option, and the program calls the matching function. This menu makes the system interactive and easy to use, while the dictionary ensures fast and efficient data handling.