
def decorator_function(string1, string2, string3) :
	reverse1 = string1[::-1]
	reverse2 = string2[::-1]
	reverse3 = string3[::-1]
	return reverse1, reverse2, reverse3

string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
string3 = input("Enter a string: ")

reverse_strings = decorator_function(string1, string2, string3)
print(reverse_strings)
