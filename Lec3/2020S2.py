def escapeRoom_dfs(row, col, grid):
      
    #print("row {}".format(row))
    #print("col {}".format(col))
    if row == len(grid) and col == len(grid[0]):
        return True

    value = grid[row-1][col-1]
    #print("value {}".format(value))
    grid[row-1][col-1] = 0
    res = False
  
    for i in range(len(grid)):
        nrow,ncol = i+1, value // (i+1)

        if value >= (i+1) and value % nrow == 0 and (ncol <= len(grid[0])):
            #print("nrow {}".format(nrow))
            #print("ncol {}".format(ncol))
            if grid[nrow-1][ncol-1] > 0 and escapeRoom_dfs(nrow, ncol, grid):
                res = True
                break
    
    for j in range(len(grid[0])):
        nrow,ncol = value // (j+1), j+1
        if value >= (j+1) and value % ncol == 0 and (nrow <= len(grid)):
            if escapeRoom_dfs(nrow, ncol, grid):
                res = True
                break     
            
    grid[row-1][col-1] = value
    return res
    


  
if __name__ == "__main__":
    # grid = [[3 ,10 ,8 , 14],
    #         [1 ,11 ,12, 12],
    #         [8 ,2  ,3 , 9]]
    M, N = int(input()), int(input())
    grid = []
    for i in range(M):
        grid.append([int(i) for i in input().split()])
    
     
    if (escapeRoom_dfs(1, 1, grid)): print("yes")
    else: print("no")
    