"""
if condition practice
"""

def ticket_price(age):
	"""
	age: int -> float
	return the ticket price for a person with age in years. 
	Seniors 65 and over pay 4.75, kids 12 and under pay 4.25 and everyone else pays 7.5
	>>> ticket_price(7)
	4.25
	>>> ticket_price(21)
	7.5
	"""
	pass


def different_types(obj1, obj2):
    """Return True iff obj1 and obj2 are of different types.
    
    >>> different_types(3, '3')
    True
    >>> different_types(108.0, 3.14)
    False
    """
    pass


if __name__ == "__main__":
	assert ticket_price(7) == 4.25, "error"
	assert ticket_price(21) == 7.5, "error"
	assert different_types(3, '3') == True, "error"
	assert different_types(108.0, 3.14) == False, "error"
	print("test passed")