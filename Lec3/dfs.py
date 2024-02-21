def dfs(grid, row, col, pos):
    target = row * col
    if target == 1:
        return True
    
    if target not in pos:
        return False
    
    if grid[row-1][col-1] < 0: # visited -> loop -> not found
        return False
    
    grid[row-1][col-1] = -grid[row-1][col-1] # we have seen this num
    
    for r,c in pos[target]:
        if dfs(grid, r, c, pos):
            return True
    return False


if __name__ == "__main__":
    M, N = int(input()), int(input())
    grid = []
    
    pos = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])): # {12: [[2,3], [2,4]]}
            pos[grid[i][j]] = pos.get(grid[i][j], []) + [[i+1,j+1]]
    if (dfs(grid, M, N, pos)): print("yes")
    else: print("no")
    