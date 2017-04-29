import random
from debug import *



def quickSort(lst):
	# call the recursive quicksort function passing in the the first and last indecies in the list
	quickSortR(lst,0,len(lst))

def quickSortR(lst, startIndex, stopIndex):
	# if you are only looking at one item in the list, return
	if stopIndex-startIndex <= 0:
		return

	# swap first and middle items in range to keep time to 0(n*Ln(n))
	midpoint = (startIndex + stopIndex) // 2
	# print("start:, ", startIndex, " end: ", stopIndex)
	# print ("midpoint: ", midpoint)
	lst[startIndex], lst[midpoint] = lst[midpoint], lst[startIndex]

	# start the swap point as the index after the start index
	swappoint = startIndex + 1
	for i in range(swappoint, stopIndex):
		# if current item is less than item at startIndex, 
			# then swap it with the item at swappoint's location
			# and increment swappoint
		# else, continue 
		if lst[i] < lst[startIndex]:
			lst[swappoint], lst[i] = lst[i], lst[swappoint]
			swappoint += 1

	# since swappoint is now the first location where the item 
	# is greater than or equal to the item at the startIndex, swap
	# the item at startIndex and the one at swappoint -1
	sortedPoint = swappoint - 1
	lst[startIndex], lst[sortedPoint] = lst[sortedPoint], lst[startIndex]


	# call quicksort on the indecies left of sortedPoint and the indecies to the right of sortedPoint
	quickSortR(lst, startIndex, sortedPoint)
	quickSortR(lst, sortedPoint + 1, stopIndex)


if __name__ == "__main__":
	j = 8
	while j < 20:
		lst  =[]
		length = j
		for k in range(length):
			lst.append(random.randint(0,length-1))
		cpy = lst[:]
		Debug("unshuffled lst: " + str(lst))
		# for i in range(len(lst)):
		# 	r = random.randint(0,len(lst)-1)
		# 	lst[i], lst[r] = lst[r], lst[i]
		Debug("unshuffled lst: " + str(lst))
		
		quickSort(lst)

		print ("my sort: ", lst)
		print ("pythons sort: ", sorted(lst))
		if (lst != sorted(lst)):
			print("Quicksort didn't work!!")
			print ("my sort: ", lst)
			print ("pythons sort: ", sorted(lst))
			print()
			print()
		else:
			pass
			# print (j, ": success!\n\n")
		j*=2

