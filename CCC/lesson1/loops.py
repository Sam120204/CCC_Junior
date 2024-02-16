"""
loops practice
"""

def all_harrypotter(s):
	"""
	return true if every character in s appear in harrypotter
	>>> all_harrypotter('hao')
	True
	>>> all_harrypotter('terror')
	True
	>>> all_harrypotter('happy')
	False
	"""
	pass


def find_letter_n_times(string, letter, n):
	"""
	return the smallest substring of s starting from index 0 that contains n occurances of letter
	no case-sensitive, letter appears at least n times
	>>> find_letter_n_times('UforseEducation', 'u', 2)
	'UforseEdu'
	"""
	pass


def generate_table():
	"""
	use for loops to generate a table
	"""
	pass



if __name__ == "__main__":
	assert all_harrypotter('terror') == True, "all_harrypotter error"
	assert find_letter_n_times('UforseEducation', 'u', 2) == "UforseEdu", "find_letter_n_times error"
	print("test passed")
	generate_table()
