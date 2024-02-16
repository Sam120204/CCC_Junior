# Question 1 Solution

def J1_2020_Sol():
    small = int(raw_input())
    medium = int(raw_input())
    large = int(raw_input())
    
    if small + medium * 2 + large * 3 >= 10:
        print("happy")
    else:
        print("sad")

# Question 2 Solution

def J2_2020_Sol():
    p = int(raw_input())
    n = int(raw_input())
    r = int(raw_input())
    
    total = n
    cur_infected = n
    day = 0
    while total <= p:
        day += 1
        cur_infected *= r
        total += cur_infected
    print day


# Question 3 Solution
def J3_2020_Sol():
    lines = int(raw_input())
    left, right, top, bottom = float('inf'), 0, float('inf'), 0
    for i in range(lines):
        point = raw_input()
        x, y = int(point.split(',')[0]), int(point.split(',')[1])
        if x < left:
            left = x
        if x > right:
            right = x
        if y < top:
            top = y
        if y > bottom:
            bottom = y
    print(str(left-1) + "," + str(top-1))
    print(str(right+1) + "," + str(bottom+1))

# Question 4 answer

def J4_2020_Sol():
    t = raw_input()
    s = raw_input()
    all_cyclic_shift = [s]
    for i in range(len(s)-1):
        s = s[1:] + s[0]
        all_cyclic_shift.append(s)
        
    for shifted_s in all_cyclic_shift:
        if shifted_s in t:
            print "yes"
            return
    print "no"

# Question 5 answer
'''

Idea: 
Use dfs. If the concept of dfs has not been introduced to students, please introduce it before
doing this question. 
The question wants us to get to the bottom right corner. So we want to find a cell,
whose value is m * n, then the problem become finding such cell, and finding 
another cell that leads us to that cell, ..., which essentially is finding 
a path from the bottom right corner to the top left corner given the jumping rule.

'''

def dfs(start, target, board, m, n, visited):
    # base case: we found a path from the end to the start
    if target == start: return True
    for i in range(m):
        for j in range(n):
        	# found the target in this run
            if board[i][j] == target:
            	# make sure we are not running into cycles
                if (i,j) not in visited:
                    visited.add((i, j))
                    # change the target to (i+1) * (j+1), the position of
                    # the current cell that leads to our previous target
                    # if this returns true, then there is a path from this cell
                    # to the start
                    if dfs(start, (i+1) * (j+1), board, m, n, visited) == True:
                        return True
    return False
    
def J5_2020_Sol():
    m = int(raw_input())
    n = int(raw_input())
    board = []
    # building the board
    for i in range(m):
        row = raw_input().split()
        row = map(int, row)
        board.append(row)
    
    # calling dfs
    if dfs(board[0][0], m*n, board, m, n, set()):
        print "yes"
    else:
        print "no"
    

    