def decorators(*args, **kwargs) :
	def wrapper_function(func):
		func()
		print(args[::-1])
	return wrapper_function


def reverse_strings():
	print("Reversing order!")

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")

decorators(string1,string2,string3)(reverse_strings)

