def result() :
	num1 = int(input("Enter a value:"))

	operator = input("Enter Operator:")

	num2 = int(input("Enter a value:"))

	


	if operator == "+":
		print (num1 + num2)

	elif operator == "-":
		print(num1 - num2)

	elif operator == "*":
		print (num1 * num2)

	elif operator == "/":
		print(num1 / num2)

	elif operator == "**":
		print(num1 ** num2)

	else:
		print("Invalid Choice")
		
		return result()