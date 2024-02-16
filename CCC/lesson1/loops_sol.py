"""
loops practice solution
"""



def all_harrypotter(s):
	for ch in s:
		if not (ch in 'harrypotter'):
			return False
	return True



def find_letter_n_times(string, letter, n):
	count = 0
	result = ""
	for s in string:
		if s.lower() == letter.lower():
			count = count + 1
		result = result + s
		if count == n:
			break
	return result


def generate_table():
	print "n", "\t", "2**n"
	print "---", "\t", "----"
	for x in range(13):
		print x, "\t", 2**x



if __name__ == "__main__":
	assert all_harrypotter('terror') == True, "all_harrypotter error"
	assert find_letter_n_times('UforseEducation', 'u', 2) == "UforseEdu", "find_letter_n_times error"
	print("test passed")
	generate_table()