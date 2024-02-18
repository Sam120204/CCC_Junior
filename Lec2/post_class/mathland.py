import sys
from collections import deque

# Input handling
input = sys.stdin.readline
n, k = map(int, input().split())

# Grid initialization
grids = [[] for _ in range(4)]  # Four grids for each rotation

# Reading the initial grid
for i in range(n):
    grids[0].append(list(input().strip()))  # Strip to remove newline characters

# Grid rotation function
def rotate(grid):
    return [[grid[n-j-1][i] for j in range(n)] for i in range(n)]

# Store all rotations of the grid
for i in range(1, 4):
    grids[i] = rotate(grids[i-1])

# Flatten function to convert node to a unique index
def flat(node):
    return node[0][0] * n * 4*k + node[0][1] * 4*k + node[1]

# Distance array initialization
dist = [-1 for _ in range(n*n * 4 * k + 1)]
start = ((0, 0), 0)

# Find the start position and exit position (not used)
for i in range(n):
    for j in range(n):
        if grids[0][i][j] == "E":
            start = ((i, j), 0)

# BFS initialization
q = deque([start])
dist[flat(start)] = 0
found = False

# BFS loop
while q:
    curr = q.popleft()
    pos, steps = curr
    
    # Determine which rotated grid we're on based on the number of steps
    gridIdx = steps % (4*k) // k
    nextGridIdx = (steps+1) % (4*k) // k

    # If we're at the exit, print the distance and exit the loop
    if grids[gridIdx][pos[0]][pos[1]] == "X":
        found = True
        print(dist[flat(curr)])
        break

    # Define possible movements: up, down, left, right
    edges = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_pos = (pos[0] + dx, pos[1] + dy)
        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n:  # Check bounds
            # If the next position is not a wall, add it to edges
            if grids[nextGridIdx][new_pos[0]][new_pos[1]] != "W":
                edges.append((new_pos, (steps+1) % (4*k)))

    # Process edges and update distances
    for edge in edges:
        if dist[flat(edge)] == -1:  # If the node has not been visited
            dist[flat(edge)] = dist[flat(curr)] + 1
            q.append(edge)

# If the exit was not found, print -1
if not found:
    print(-1)

