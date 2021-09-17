name = input("Enter your name here: ")
age = int(input("Enter your age here: "))

if age < 18:
	print("Sorry ", name," is not eligible to vote")
else:
	print(name, "is eligible to vote!")
