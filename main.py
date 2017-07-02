
def load_names():
	with open("namepool.txt") as namepool_file:
		names = namepool_file.read().split("\n")

	while "" in names:  # In case of newline at end of file
    	names.remove("")
    	
	return names

temp = load_names()
for t in temp:
	print(t)