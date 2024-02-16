
def j3_2016(word):
	if isPalindrome(word):
		return len(word)
	maxLength = 1
	for i in range(len(word)-1):
		length = longestPalindrome(word[i:])
		if length > maxLength:
			maxLength = length
	return maxLength


def longestPalindrome(word):
	if len(word) == 1:
		return 1
	for i in range(len(word), 1, -1):
		if isPalindrome(word[:i]):
			return i
	return 1



def isPalindrome(word):
	if len(word) == 1:
		return True
	for i in range(len(word)/2):
		front = word[i]
		back = word[len(word)-1-i]
		if front != back:
			return False
	return True



if __name__ == "__main__":
	testWord = raw_input()
	print(j3_2016(testWord))