# Name: Eli Thomas
# Date: 9/18/2024
# File Purpose: Add extra functionality for contact list (telephones)

contact_dict_ = {}

def print_list():
	"""lists contacts"""
	print("=================== CONTACT LIST ======================")
	print("Last Name             First Name	     Phone")
	print("====================  ====================   ==========")
	for ID in contact_dict_:
		print("{:<21} {:<22} {:<22}".format(contact_dict_[ID][1], contact_dict_[ID][0], ID))

def add_contact(contact_dict, ID_ = 0, first_name = "N/A", last_name = "N/A"):
	"""adds a contact to end of list"""
	try:
		if ID_ in contact_dict_: 
			print("error.")
		else: 
			contact_dict[ID_] = [first_name, last_name]
			print("Added:", first_name, last_name)
		return contact_dict[ID_]
	except:
		print("Invalid input.")

def modify_contact(contact_dict, ID_ = 0, first_name = "N/A", last_name = "N/A"):
	"""modify a contact within a valid index range"""
	try:
		if ID_ in contact_dict_:
			contact_dict[ID_] = [first_name, last_name]
			print("Modified: ", first_name, last_name)
		else:
			print("error.")
		return contact_dict[ID_]
	except:
		print("Invalid input.")
	
def delete_contact(contact_dict, index = 0):
	"""delete contact within valid index range"""
	try:
		if index < 0 or int(index) >= len(contact_dict):
			print("Invalid index number.")
			return False
		contact_dict.pop(index)
		return True
	except:
		print("Invalid input.")
		
def sort_contacts(contact_dict, column=0):
	"""If column is 0, sort by first name, else, sort by last name"""
	if column == 0:
		contact_dict.sort()
	elif column == 1:
		contact_dict.sort(key=lambda contact_dict: contact_dict[1])
	
def print_menu():
	"""GUI for program"""
	print("\n     *** TUFFY TITAN CONTACT MAIN MENU ***     ")
	print("1. Add contact")
	print("2. Modify contact")
	print("3. Delete contact")
	print("4. Print list")
	print("5. Sort list")
	print("6. Exit program\n")
	return
