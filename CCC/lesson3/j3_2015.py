allLetters = "abcdefghijklmnopqrstuvwxyz"
allVowels = "aeiou"


def convertCharacter(ch):
	if ch in allVowels:
		return ch
	letters = ch
	curr_pos = allLetters.index(ch)
	prev_vowel_pos = findVowelBefore(curr_pos)
	next_vowel_pos = findVowelAfter(curr_pos)
	if prev_vowel_pos == curr_pos:
		letters = letters + allLetters[next_vowel_pos]
	elif next_vowel_pos == curr_pos:
		letters = letters + allLetters[prev_vowel_pos]
	else:
		prev_diff = curr_pos - prev_vowel_pos
		next_diff = next_vowel_pos - curr_pos
		if prev_diff < next_diff:
			letters = letters + allLetters[prev_vowel_pos]
		elif prev_diff > next_diff:
			letters = letters + allLetters[next_vowel_pos]
		else:
			letters = letters + allLetters[prev_vowel_pos]
	next_consonant = allLetters[getNextConsonant(curr_pos)]
	letters += next_consonant
	return letters


def findVowelBefore(curr_pos):
	prev_pos = curr_pos
	for idx in range(curr_pos, -1, -1):
		if allLetters[idx] in allVowels:
			prev_pos = idx
			break
	return prev_pos


def findVowelAfter(curr_pos):
	next_pos = curr_pos
	for idx in range(curr_pos, len(allLetters)):
		if allLetters[idx] in allVowels:
			next_pos = idx
			break
	return next_pos


def getNextConsonant(curr_pos):
	next_pos = curr_pos
	for idx in range(curr_pos+1, len(allLetters)):
		if allLetters[idx] not in allVowels:
			next_pos = idx
			break
	return next_pos


def translateWord(word):
	newWord = ""
	for ch in word:
		if ch not in allVowels:
			newCh = convertCharacter(ch)
			newWord += newCh
		else:
			newWord += ch
	return newWord


if __name__ == "__main__":
	word = raw_input()
	print(translateWord(word))