"""
if condition practice solution
"""


def ticket_price(age):
	if age >= 65:
		return 4.75
	elif age <= 12:
		return 4.25
	else:
		return 7.5



def different_types(obj1, obj2):
	if type(obj1) != type(obj2):
		return True
	else:
		return False
	# return type(obj1) != type(obj2)



if __name__ == "__main__":
	assert ticket_price(7) == 4.25, "error"
	assert ticket_price(21) == 7.5, "error"
	assert different_types(3, '3') == True, "error"
	assert different_types(108.0, 3.14) == False, "error"
	print("test passed")