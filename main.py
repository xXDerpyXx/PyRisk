
def LoadNames():
	with open("namepool.txt") as namepool_file:
	    names = namepool_file.read().split("\n")
	    return names