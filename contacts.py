# Name: Eli Thomas
# Date: 9/18/2024
# File Purpose: Add extra functionality for contact list (telephones)

contact_dict_ = {}

def print_list():
	"""lists contacts"""
	print("=================== CONTACT LIST ======================")
	print("Last Name             First Name	     Phone")
	print("====================  ====================   ==========")
	for id in contact_dict_:
		print("{:<21} {:<22} {:<22}".format(contact_dict_[id][1], contact_dict_[id][0], id))

def add_contact(contact_dict, id = 0, first_name = "N/A", last_name = "N/A"):
	"""adds a contact to end of list"""
	try:
		if id in contact_dict: 
			return "error"
		else: 
			contact_dict[id] = [first_name, last_name]
			print("Added:", first_name, last_name)
			return contact_dict[id]
	except:
		print("Invalid input.")

def modify_contact(contact_dict, id = 0, first_name = "N/A", last_name = "N/A"):
	"""modify a contact within a valid index range"""
	try:
		if id in contact_dict:
			contact_dict[id] = [first_name, last_name]
			print("Modified: ", first_name, last_name)
			return contact_dict[id]
		else:
			print("error.")
	except:
		print("Invalid input.")
	
def delete_contact(contact_dict, id = 0):
	"""delete contact within valid index range"""
	try:
		if id in contact_dict:
			return_val = [id[0], id[1]]
			contact_dict.pop(id)
		else:
			return "error"
	except:
		print("Invalid input.")
		
def sort_contacts(contact_dict):
	"""If """
	list_temp = []
	for key, value in contact_dict.items():
		list_temp.append([key, value[0], value[1]])
		list_temp.sort(key = lambda x: [x[2], x[1]])
	contact_dict.clear()
	for value in list_temp:
		contact_dict[value[0]] = [value[1], value[2]]
		
		
	contact_dict = sorted(contact_dict.items())
	
def find_contact(contact_dict, find = 0):
	search_dict = {}
	
	"""search_dict[find] = contact_dict[find]"""
	if find.isnumeric():
		find = int(find)
		if find in contact_dict:
			search_dict[find] = contact_dict[find]
	
	else:
		for key, value in contact_dict.items():
			if find in value[0] or find in value[1]:
				search_dict[key] = [value[0], value[1]]
				search_dict[key] = contact_dict[key]

	print("================== FOUND CONTACT(S) ===================")
	print("Last Name             First Name	     Phone")
	print("====================  ====================   ==========")
	for ID in search_dict:
		print("{:<21} {:<22} {:<22}".format(search_dict[ID][1], search_dict[ID][0], ID))
	
	return search_dict
	
			
def print_menu():
	"""GUI for program"""
	print("\n     *** TUFFY TITAN CONTACT MAIN MENU ***     ")
	print("1. Add contact")
	print("2. Modify contact")
	print("3. Delete contact")
	print("4. Print list")
	print("5. Sort list")
	print("6. Find contact")
	print("7. Exit program\n")
	return
