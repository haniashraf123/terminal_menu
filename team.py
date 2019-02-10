from cal import result
from create_memo import file
from read_memo import read
#from calcul import *
print ("  _____ _           _                                              _                __ ")
print ("/ ____| |         | |                                   /\       | |              / _| ")
print ("| (___ | |__   __ _| |__  _ __ ___ _   _  __ _ _ __     /  \   ___| |__  _ __ __ _| |_ ")
print (" \___ \| '_ \ / _` | '_ \| '__/ _ \ | | |/ _` | '__|   / /\ \ / __| '_ \| '__/ _` |  _|")
print ("____) | | | | (_| | | | | | |  __/ |_| | (_| | |     / ____ \\__ \ | | | | | (_| | | | ")
print ("|_____/|_| |_|\__,_|_| |_|_|  \___|\__, |\__,_|_|    /_/    \_\___/_| |_|_|  \__,_|_|  ")
print ("                                   __/ |                                               ")
print ("                                   |___/                                               ")



def options():
	print ("--------------------------------------")
	print("1:Terminal Calculator")
	print("2:Write Memo")
	print("3:Read Memo")
	print("4:GUI Calculator")
	print("Exit")
	choice = input("Select an option:")
	if choice == "1":
			result()
			options()
			

	elif choice == "2":
		file()
		options()

	elif choice == "3":
		read()
		options()
	if choice == "4":
		call()
		options()
		
		
	
def logins():
	print("Welcome to the private server")
	username = input("Enter Username: ")
	password = input("Enter Password: ")

	if password == "1":
		print ("Welcome Master")
		print ("--------------------------------------")
		print("1:Use Calculator")
		print("2:Write Memo")
		print("3:Read Memo")
		print("Exit")

		
		choice = input("Select an option:")

		if choice == "1":
			result()
			options()
			

		elif choice == "2":
			file()
			options()

		elif choice == "3":
			read()
			options()


	else :
		print("Invalid Username and Password")	
		print("Quitting .....")





