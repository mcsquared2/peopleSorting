import people, quickSort, random, time	
from debug import *
def shuffle(lst, numShuffles):
	for i in range(numShuffles):
		for i in range(len(lst)):
			r  = random.randint(0,len(lst)-1)
			lst[i], lst[r] = lst[r], lst[i]


def testOrderedPersons():
	names = [
		"a",
		"a",
		"a",
		"a",
		"a",
		"a",
		"a",
		"aa",
		"aa",
		"b",
		"bc",
		"ba",
		"captain kirk",
		"Godzilla",
		"d'Artigan",
		"Things that go bump",
		"Lydia Liliʻu Loloku Walania"
		]
	ages = [
		5,
		5,
		6,
		4,
		0,
		5,
		100,
		200,
		75,
		13,
		12,
		1,
		1,
		1,
		1,
		1
		]
	lst = []
	length = 15
	for i in range(length):
		lst.append(people.OrderedPerson(names[i], ages[i], "things", i))
	shuffle(lst, 5)
	print("Shufffled List::::::::::::::::::")
	for i in lst:
		print(str(i))
	quickSort.quickSort(lst)

	print("Sorted List ::::::::::::::::::::::")
	for i in lst:
		print(str(i))

def convertPersonsToOrdered(lst):
	newLst = []
	for i in range(len(lst)):
		newLst.append(people.OrderedPerson(lst[i].name, lst[i].age, lst[i].ssn, i))
	return newLst

def convertOrderedToPersons(lst):
	newLst = []
	for i in range(len(lst)):
		newLst.append(people.Person(lst[i].name, lst[i].age, lst[i].ssn))
	return newLst

def createPersons(length):
	names = [
		"a",
		"aa",
		"b",
		"bc",
		"ba",
		"captain kirk",
		"Godzilla",
		"d'Artigan",
		"Things that go bump",
		"Lydia Liliʻu Loloku Walania"
		]
	lst = []
	# length = 15
	for i in range(length):
		lst.append(people.Person(names[random.randint(0, len(names)-1)], 
										random.randint(1,5), 
										"things"))
	shuffle(lst, 5)
	return lst

def sortPersons(lst):
	lst = convertPersonsToOrdered(lst)
	Debug("Unshuffled OrderedPerson List :::::::::::::")
	printList(lst)

	quickSort.quickSort(lst)
	Debug("Sorted Ordered Person List :::::::::::::::::::::")
	printList(lst)

	return convertOrderedToPersons(lst)



def main():
	# testOrderedPersons()
	startTime = time.time()
	lst = createPersons(15)
	Debug("Unshuffled Person List :::::::::::::::::")
	printList(lst)
	
	lst = sortPersons(lst)
	stopTime = time.time()
	print("Final Sorted List ::::::::::::::::")
	printList(lst, True)
	print("Time taken: ", stopTime - startTime, " seconds")
	
	

main()