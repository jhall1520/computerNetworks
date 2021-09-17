linksTuple =  [("(1,2)", "10Mbps"), ("(2,3)", "5Mbps"), ("(3,4)",
	"10Mbps")]

links = dict(linksTuple) 

link = input("Enter the link: ")

bandwidth = links[link]

print("Bandwidth for link between h" + link[1] + " and h" + link[3] 
	+ " is " + bandwidth)


