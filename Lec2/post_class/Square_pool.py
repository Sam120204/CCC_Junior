n = int(input())
t = int(input())
yard = [['' for col in range(n)] for row in range(n)]
trees = []
pool_size = n-1
for i in range(t):
    location_in = input().split(' ')
    loc_x, loc_y = int(location_in[0])-1, int(location_in[1])-1
    trees.append([loc_x, loc_y])
    yard[loc_x][loc_y] = '1'
    

def check_has_tree(in_size, in_row, in_col):
    global trees
    for tree in trees:
        if in_row <= tree[0] <= in_row + in_size - 1 and in_col <= tree[1] <= in_col + in_size - 1:
            return True
    return False   

def check(in_size, in_row, in_col):
    has_trees = check_has_tree(in_size, in_row, in_col)
    if not has_trees:
        return True
    while in_size + in_row < n:
        while in_size + in_col + 1 < n: # shift col to the right  
            in_col += 1
            has_trees = check_has_tree(in_size, in_row, in_col)
            if not has_trees:
                return True
        in_row += 1
        in_col = 0
    return False


success = check(pool_size, 0, 0) # start from [0][0]
while not success:
    pool_size -= 1
    success = check(pool_size, 0, 0)
print(pool_size)
