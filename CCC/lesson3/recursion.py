def listSum(numList):
	"""
	calculating the sum of a list
	"""
	theSum = 0
	for i in numList:
		theSum = theSum + i
	return theSum


def listSum2(numList):
	"""
	use recursion to solve
	"""
	if len(numList) == 1:
		return numList[0]
	else:
		return numList[0] + listSum2(numList[1:])


def listSum3(numList):
	theSum = 0
	for aList in numList:
		for num in aList:
			theSum = theSum + num
	return theSum


def listSum4(numList):
	theSum = 0
	for aListList in numList:
		for aList in aListList:
			for num in aList:
				theSum = theSum + num
	return theSum


def listSum3(numList):
	theSum = 0
	for aList in numList:
		theSum = theSum + listSum(aList)
	return theSum


def listSum4(numList):
	theSum = 0
	for aListList in numList:
		theSum = theSum + listSum3(aListList)
	return theSum


def finalSum(numbers):
	"""
	final sum algorithm. Use recursion to solve the nested list problem
	"""
	if isinstance(numbers, int):
		return numbers
	else:
		theSum = 0
		for aList in numbers:
			theSum = theSum + finalSum(aList)
	return theSum


def doDuplication(nestedList):
	"""
	return a new nested list with all the numbers in the nestedList duplicated 
	each integer should appear twice. The structure should be the same as the input, only with 
	some new numbers added 
	if nestedList is an int, return a list of 2 copies of it
	>>> doDuplication(1)
	[1, 1]
	>>> doDuplication([])
	[]
	>>> doDuplication([1, 2])
	[1, 1, 2, 2]
	>>> doDuplication([1, [2, 3]])
	[1, 1, [2, 2, 3, 3]]
	"""
	if isinstance(nestedList, int):
		return [nestedList, nestedList]
	else:
		if len(nestedList) == 0:
			return []
		retList = []
		for aList in nestedList:
			if isinstance(aList, int):
				retList += doDuplication(aList)
			else:
				retList += [doDuplication(aList)]
		return retList


def addOneToList(nestedList):
	"""
	add 1 to every number in the nested list
	if nestedList is a int, do nothing
	if it is a list, add 1 to each number
	>>> addOneToList(1)
	1
	>>> addOneToList([])
	[]
	>>> addOneToList([1, [2, 3], [[5]]])
	[2, [3, 4], [[6]]]
	"""
	if isinstance(nestedList, int):
		return nestedList
	else:
		if len(nestedList) == 0:
			return []
		retList = []
		for aList in nestedList:
			if isinstance(aList, int):
				retList.append(aList+1)
			else:
				retList.append(addOneToList(aList))
		return retList



if __name__ == "__main__":
	#print(listSum([1, 3, 5, 7, 9]))
	#print(listSum2([1, 3, 5, 7, 9]))
	#print(finalSum([[1, [2]], [[[3]]], 4, [[5, 6], [[[7], 8], [9, 10]]]]))
	#print(doDuplication(1))
	#print(doDuplication([1, 2]))
	#print(doDuplication([1, [2, 3]]))
	#print(doDuplication([[1, 2, [4]], [2, 3], 5]))
	print(addOneToList(1))
	print(addOneToList([]))
	print(addOneToList([1, [2, 3], [[5]]]))
	print(addOneToList([1, [2, 3], [[5], [6]], 7]))