# Name: Eli Thomas
# Date: 9/18/2024
# File Purpose: Main driver for contact menu (with telephone #'s)

from contacts import *

exit_program = False

while exit_program == False:

	print_menu()

	choice = input("Enter menu choice: ")
	print("")
	
	if choice == '4':
		sort_contacts(contact_dict_)
		print_list()
		
	elif choice == '1':
		try:
			ID = int(input("Enter phone number: "));
			first = input("Enter first name: ")
			last = input("Enter last name: ")
			add_contact(contact_dict_, ID, first, last)
		except:
			print("Invalid input.")
			
	elif choice == '2':
		if len(contact_dict_) == 0:
			print("List is empty!")
			continue
		ID = int(input("Enter phone number: "))
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		modify_contact(contact_dict_, ID, first, last)
		
	elif choice == '3':
		ID = int(input("Enter telephone number: "))
		delete_contact(contact_dict_, ID)
		
	elif choice == '5':
		search = input("Enter search string: ")
		find_contact(contact_dict_, search)
		
	elif choice == '6':
		exit_program = True
	
	else:
		print("Invalid input.")
