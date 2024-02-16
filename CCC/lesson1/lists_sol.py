"""
list practice solution
"""


def biggest_difference(nums1, nums2):
	curr_max = abs(nums1[0] - nums2[0])
	for i in range(1, len(nums1)):
		diff = abs(nums1[i] - nums2[i])
		if diff > curr_max:
			curr_max = diff
	return curr_max



def sumUntilEven(lst):
	if len(lst) == 0:
		return 0
	res = 0
	for e in lst:
		if e % 2 == 1:
			res = res + e
		else:
			break
	return res



if __name__ == "__main__":
	assert biggest_difference([1, 2, 3], [6, 8, 10]) == 7, "error"
	assert biggest_difference([1, -2, 3], [-6, 8, 10]) == 10, "error"
	assert sumUntilEven([1, 3, 4, 5, 6]) == 4, "error"
	assert sumUntilEven([11, 13, 5, 3, 2, 8]) == 32, "error"
	print("test passed")