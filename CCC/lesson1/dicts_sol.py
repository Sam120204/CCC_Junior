"""
dictionary practice
"""

def build_placements(shoes):
    aDict = {}
    for idx in range(len(shoes)):
        shoe = shoes[idx]
        if shoe in aDict:
            aDict[shoe].append(idx+1)
        else:
            aDict[shoe] = [idx+1]
    return aDict



if __name__ == "__main__":
    assert build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', 'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics']) \
    == {'Saucony': [1, 5, 9], 'Asics': [2, 3, 7, 10], 'NB': [4], 'Nike': [6], 'Adidas': [8]}, "error"
    print("test passed")