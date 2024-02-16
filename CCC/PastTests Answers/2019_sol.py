# Question 1 Answer

def J1_2019_Sol():
    A_points = 0
    A_points += int(raw_input()) * 3
    A_points += int(raw_input()) * 2
    A_points += int(raw_input())
    
    B_points = 0
    B_points += int(raw_input()) * 3
    B_points += int(raw_input()) * 2
    B_points += int(raw_input()) 
    
    if A_points > B_points: 
        print('A')
    elif B_points > A_points:
        print('B')
    else:
        print('T')

# Question 2 Answer

# Note: Since the question wants us to print without newline or space,
# we have to use sys.stdout.write in python2. Since print in python2
# will print to a different line; print ..., (print variable_name followed by a comma)
# however, will print on the same line, but with an extra space.

# In python3, we can use print(abc, end="") to avoid the newline or the space.
import sys
def J2_2019_Sol():
    lines = int(raw_input())
    inputs = []
    for i in range(lines):
        line = raw_input()
        times, symbol = int(line.split()[0]), line.split()[1]
        for j in range(times):
            sys.stdout.write(symbol)
        print # print the newline


# Question 3 Answer
# As mentioned in question 2 notes, we can use print with an extra comma 
# to print the space
def J3_2019_Sol():
    lines = int(raw_input())
    for i in range(lines):
        line = raw_input()
        start, end = 0, 1
        while start < len(line):
            while end < len(line) and line[start] == line[end]:
                end += 1
            print(end-start),
            print(line[start]),
            start = end
        print # print the newline


# Question 4 Answer
"""
idea: only 2 methods are needed in this case - horizontal flip and vertical flip
implementation: swap the numbers in the list
"""

def h_flip(numbers):
    temp = numbers[0][0]
    numbers[0][0] = numbers[1][0]
    numbers[1][0] = temp
    temp = numbers[0][1]
    numbers[0][1] = numbers[1][1]
    numbers[1][1] = temp


def v_flip(numbers):
    temp = numbers[0][0]
    numbers[0][0] = numbers[0][1]
    numbers[0][1] = temp
    temp = numbers[1][0]
    numbers[1][0] = numbers[1][1]
    numbers[1][1] = temp

def J4_2019_Sol():
    numbers = [['1', '2'], ['3', '4']]
    line = raw_input()
    for ch in line:
        if ch == 'H':
            h_flip(numbers)
        else:
            v_flip(numbers)
    print(numbers[0][0] + ' ' + numbers[0][1])
    print(numbers[1][0] + ' ' + numbers[1][1])


# Question 5 Answer

# Idea: 
'''
Use dfs to do the search, since we care about the path. We start by the starting
string given, and for each substring of it, if it matches with a starting point 
of a substitution rule, we do the substitution, and start again from there. 
The base case of the recursion is that we found the ending string, 
and we used the required amount of steps. 
If we use too many steps, it doesn't matter what we found, the answer will be invalid. 
'''

def dfs(start, end, d, res, path, steps):
    # base case of the recursion: we found the answer
    if start == end and len(path) == steps: 
        res.append(path)
        return 
    
    # another base case: we used too many steps, all the answers forward will be invalid
    if len(path) >= steps: return
    
    # do the recursion: if a substring of the start matches a starting point of the 
    # substitution rule, we do the substitution and start again from there
    for i in range(len(start)):
        for j in range(i, len(start)+1):
            if start[i:j] in d.keys():
                new_start = start[:i] + d[start[i:j]][1] + start[j:]
                # call the recursive function with new start, and the path it goes through
                dfs(new_start, end, d, res, path + [str(d[start[i:j]][0]) + " " + str(i + 1) + " " + new_start], steps)

def J5_2019_Sol():
    rule1 = raw_input().split()
    rule2 = raw_input().split()
    rule3 = raw_input().split()
    
    d = {}
    d[rule1[0]] = (1, rule1[1])
    d[rule2[0]] = (2, rule2[1])
    d[rule3[0]] = (3, rule3[1])
    
    last_line = raw_input().split()
    steps, start, end = int(last_line[0]), last_line[1], last_line[2]
    
    res = []
    dfs(start, end, d, res, [], steps)
    # found the solution
    if res:
        # we take the first one (any valid solution will work here)
        for line in res[0]:
            print line

