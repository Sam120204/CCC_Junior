def escapeRoom_bfs(row,column,grid):
    pos = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pos[grid[i][j]] = pos.get(grid[i][j], []) + [[i+1,j+1]]
            
            """
            if grid[i][j] not in pos:
                pos[grid[i][j]] = [[i+1,j+1]]
            else:
                pos[grid[i][j]].append([i+1,j+1])
            """
            
    # 1. found way back to origin 
    # 2. no more path to choose
    # 3. have visited next possible path
    level = [[row, column]]
    
    while level:
        size = len(level)
        
        for i in range(size):
            r,c = level[i][0]-1,level[i][1]-1
            if grid[r][c] > 0:
                target = (r+1)*(c+1)
                if target == 1:
                    return True
                grid[r][c] = -grid[r][c]
                if target in pos:
                    level = level + pos[target]
        
        level = level[size:]

    return False


  
if __name__ == "__main__":
    # grid = [[3 ,10 ,8 , 14],
    #         [1 ,11 ,12, 12],
    #         [8 ,2  ,3 , 9]]
    M, N = int(input()), int(input())
    grid = []
    for i in range(M):
        grid.append([int(i) for i in input().split()])
    
    
    gridCopy = []
    
    for row in grid:
        gridCopy.append(row[::])
    
    if (escapeRoom_bfs(M,N,gridCopy)): print("yes")
    else: print("no")

