"""
dictionary practice
"""

def build_placements(shoes):
    """Return a dictionary where each key is a company and each value is a
    list of placements by people wearing shoes made by that company.
    
    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', \
    'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}
    """
    pass






if __name__ == "__main__":
    assert build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', 'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics']) \
    == {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}, "error"
    print("test passed")