debugBool = False
# debugBool = True

def Debug(msg):
	if (debugBool):
		print(msg)

def printList(lst, b = debugBool):
	if (b):
		for i in lst:
			print(str(i))