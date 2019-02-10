import os


def read():
	os.chdir('/Users/hani/Desktop/projects/files/text/')
	print(os.listdir())
	print("1:Text")
	print("2:Text 1")
	choice = input("Select a memo to read: ")
	if choice == "1":
		file = open("/Users/hani/Desktop/projects/files/text/text1.txt")
		print (file.read())
		file.close
	elif choice == "2":
		file = open("/Users/hani/Desktop/projects/files/text/text.txt")
		print (file.read())
		file.close
	else:
		print("Invalid Option")
		