# Question 1 Solution

def J1_2018_Sol():
  #a = int(raw_input()) 
  #b = int(raw_input()) 
  #c = int(raw_input()) 
  #d = int(raw_input()) 
  import sys 
  input = sys.stdin.readline
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  if (a == 8 or a == 9) and (d == 8 or d == 9) and b == c: 
    print("ignore") 
  else: 
    print("answer")  


# Question 2 Solution
def J2_2018_Sol():
  import sys 
  input = sys.stdin.readline 
  N = int(input()) 
  lot = ["C" for j in range(N)] # Create a list size of N, each element is "C"
  yesterday = input() 
  for i in range(len(yesterday)):
    if (yesterday[i] == '.'): 
      lot[i] = '.'
  today = input()
  for i in range(len(today)): 
    if (today[i] == '.'): 
      lot[i] = '.' 
  print(str(lot.count('C')))


# Question 3 Solution
def J3_2018_Sol():
  import sys 
  input = sys.stdin.readline 
  D = map(int, input().strip().split())
  dist = [[0 for j in range(5)] for i in range(5)] # create a 2D list
  for i in range(5): 
    for j in range(i + 1, 5, 1): 
      dist[i][j] = dist[i][j - 1] + D[j - 1] 
    for j in range(i - 1, -1, -1): 
      dist[i][j] = dist[i][j + 1] + D[j] 
  for i in range(5):
    for j in range(5):
      print(dist[i][j]),
    print



# Question 4 Solution

# idea: first we build the grid. By reading from stdout and cast each line of input string 
# to int, we have a 2d list as our grid (at the end of line 15). 
# Since we know that "The leftmost column is the first measurement for each sunflower, and the rightmost column is the last measurement for each sunflower. If a sunflower was smaller than another when initially planted, it remains smaller for every measurement.",
# and the grid is only modified through rotation,
# we only need to compare the position of the smallest number in the grid. 
# while the smallest number in the grid is not at the top left corner, we keep rotating until
# it is placed in the top left corner. 


def rotate(grid):
    # :: is a special kind of slicing in python. 
    # it means slicing the list by jumping the number after the double colon.
    # ex: grid[::3] means "nothing for the first, nothing for the second, jump by three"
    # thus, grid[::-1] means reverse the order of the grid list
    grid = zip(*grid[::-1])
    return grid

def J4_2018_Sol():
    lines = int(raw_input()) # input() for python3
    grid = []
    for i in range(lines):
        line = raw_input().split() # input line is a string, split into a list of strings
        line = map(int, line) # make each element an int
        grid.append(line)
    
    # we know that the upper left corner should hold the initial growth of the 
    # smallest sunflower, so that should match the smallest number in the grid
    smallest = min(map(min,grid))
    
    while smallest != grid[0][0]:
    # rotate grid
        grid = rotate(grid)
    
    for line in grid:
        print(' '.join(map(str, line)))
    

# Question 5 Solution

# Idea:
'''
Use the Breath First Search algorithm. Put the first page to the queue, 
and use the queue as a starting point of the algorithm.
Find all the neighbours of the current node, and add them to the queue for further visiting.
Also, we need to keep track of all the pages that we already visited. 
We do that by using a visited set. 

At the end, when we finished the BFS, we check if all the pages are visited
by checking len(visited) == len(graph). If so, we print 'Y'; otherwise we print 'N'

The degree variable is used to find the shortest path to an end page. 
The way to update the degree variable is that we add one to it whenever we 
finished visiting one layer. 
'''
def J5_2018_Sol():
    lines = int(raw_input()) # input() for python3
    graph = {}
    for i in range(1, lines + 1):
        line = raw_input()
        next_pages = line.split()[1: ]
        next_pages = map(int, next_pages)
        graph[i] = next_pages
    # print graph
    
    if len(graph) == 1: 
        print('Y')
        print(1)
    
    # start bfs here, make sure to introduce bfs to the student first 
    queue = [1]
    visited = {1}
    degree = 0
    ended = False
    shortest_path_len = float('inf')
    while queue:
        size = len(queue)
        degree += 1
        
        # when the for loop finishes, we finished visiting a layer of neighbours 
        for i in range(size):
            # pop the queue here
            cur_page = queue.pop(0) 
            if ended == False and graph[cur_page] == []:
                ended = True
                shortest_path_len = degree 
            # loop through all the pages that we can go next from the current page
            for page in graph[cur_page]:     
                if page not in visited:
                    # add them to the queue only when we haven't visit them yet
                    visited.add(page)
                    queue.append(page)
    
    # check if every page has been visited
    if len(visited) != len(graph):
        print 'N'
    else:
        print 'Y'
    print(shortest_path_len)