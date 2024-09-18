# Name: Eli Thomas
# Date: 9/18/2024
# File Purpose: Main driver for contact menu (with telephone #'s)

from contacts import *

exit_program = False

while exit_program == False:

	print_menu()

	choice = input("Enter menu choice: ")
	print("")
	
	if choice == '1':
		print_list()
		
	elif choice == '2':
		ID = input("Enter phone number: ");
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		add_contact(contact_dict_, ID, first, last)
		
	elif choice == '3':
		if len(contact_dict_) == 0:
			print("List is empty!")
			continue
		index = int(input("Enter index to modify: "))
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		modify_contact(contact_dict_, first, last, index)
		
	elif choice == '4':
		index = int(input("Enter index to modify: "))
		delete_contact(contact_dict_, index)
		
	elif choice == '5':
		sort_contacts(contact_dict_, 0)
		
	elif choice == '6':
		sort_contacts(contact_dict_, 1)
		
	elif choice == '7':
		exit_program = True
	
	else:
		print("Invalid input.")
