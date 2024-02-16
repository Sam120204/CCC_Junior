"""
list practice
"""

def biggest_difference(nums1, nums2):
	"""
	return the greatest absolute difference between numbers at corresponding positions in nums1 and nums2
	>>> biggest_difference([1, 2, 3], [6, 8, 10])
	7
	>>> biggest_difference([1, -2, 3], [-6, 8, 10])
	10
	"""
	pass



def sumUntilEven(lst):
	"""
	Sum all elements in a list up to but not including the first even number
	>>> sumUntilEven([1, 3, 4, 5, 6])
	4
	>> sumUntilEven([11, 13, 5, 3, 2, 8])
	32
	"""
	pass



if __name__ == "__main__":
	assert biggest_difference([1, 2, 3], [6, 8, 10]) == 7, "error"
	assert biggest_difference([1, -2, 3], [-6, 8, 10]) == 10, "error"
	assert sumUntilEven([1, 3, 4, 5, 6]) == 4, "error"
	assert sumUntilEven([11, 13, 5, 3, 2, 8]) == 32, "error"
	print("test passed")