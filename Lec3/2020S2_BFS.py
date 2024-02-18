def escapeRoom_dfs(grid,row,col, pos):
    # 1. found way back to origin 
    # 2. no more path to choose
    # 3. have visited next possible path
    
    target = row * col
    if target == 1:
        return True
    
    if target not in pos:
        return False
    
    if grid[row-1][col-1] <= 0:
        return False
    
    grid[row-1][col-1] = -grid[row-1][col-1]
    
    for r, c in pos[target]:
        if escapeRoom_dfs(grid, r, c, pos):
            return True
    return False
  
  
  
if __name__ == "__main__":
    # grid = [[3 ,10 ,8 , 14],
    #         [1 ,11 ,12, 12],
    #         [8 ,2  ,3 , 9]]
    M, N = int(input()), int(input())
    grid = []
    for i in range(M):
        grid.append([int(i) for i in input().split()])


    pos = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pos[grid[i][j]] = pos.get(grid[i][j], []) + [[i+1,j+1]]
            
   
    if (escapeRoom_dfs(grid, M,N, pos)): print("yes")
    else: print("no")
    