

record = { 'username':'hani',
			'password': '1'

		 }




print ("  _____ _           _                                              _                __ ")
print ("/ ____| |         | |                                   /\       | |              / _| ")
print ("| (___ | |__   __ _| |__  _ __ ___ _   _  __ _ _ __     /  \   ___| |__  _ __ __ _| |_ ")
print (" \___ \| '_ \ / _` | '_ \| '__/ _ \ | | |/ _` | '__|   / /\ \ / __| '_ \| '__/ _` |  _|")
print ("____) | | | | (_| | | | | | |  __/ |_| | (_| | |     / ____ \\__ \ | | | | | (_| | | | ")
print ("|_____/|_| |_|\__,_|_| |_|_|  \___|\__, |\__,_|_|    /_/    \_\___/_| |_|_|  \__,_|_|  ")
print ("                                   __/ |                                               ")
print ("                                   |___/                                               ")


username = input("username: ")
password = input("Pass: ")








def login():
	global success
	success = False
	if username == record.get('username') and password == record.get('password'):
		success = True
		if success == True:
			print("Login Completed")
			print("Welcome ",record.get('username'))
		
		


	else:
		print ("Invalid Username or Password")
		print("Quitting ......")


login()

