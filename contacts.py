# Name: Eli Thomas
# Date: 9/18/2024
# File Purpose: Add extra functionality for contact list (telephones)

contact_dict_ = {}

def print_list():
	"""lists contacts"""
	print("======================== CONTACT LIST =========================")
	print("Index   Last Name             First Name	     Phone")
	print("======  ====================  ====================   ==========")
	index = 0
	for contact in contact_dict_:
		print("{:<7} {:<21} {:<1}".format(index, contact[0], contact[1]))
		index += 1

def add_contact(contact_dict, ID_ = "N/A", first_name = "N/A", last_name = "N/A"):
	"""adds a contact to end of list"""
	contact_dict.append([first_name,last_name])
	return contact_dict

def modify_contact(contact_dict, first_name = "N/A", last_name = "N/A", index = 0):
	"""modify a contact within a valid index range"""
	try:
		if index < 0 or index >= len(contact_dict):		
			print("Invalid index number.")
			return False
		contact_dict[index] = [first_name, last_name]
		return True
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
	print("1. Print list")
	print("2. Add contact")
	print("3. Modify contact")
	print("4. Delete contact")
	print("5. Sort list by first name")
	print("6. Sort list by last name")
	print("7. Exit program\n")
	return
