import os

def file():
	os.chdir('/Users/hani/Desktop/projects/files/text/')
	print(os.listdir())
	print("1:Text")
	print("2:Text 1")
	choice = input("Select a memo to write: ")
	if choice == "1":
		file = open("/Users/hani/Desktop/projects/files/text/text1.txt", "w+")
		memo = input("Type Your Memo: ")
		file.write(memo)
		file.close
	elif choice == "2":
		file = open("/Users/hani/Desktop/projects/files/text/text.txt", "w+")
		memo = input("Type Your Memo: ")
		file.write(memo)
		file.close
	else:
		print("Invalid Option")
		