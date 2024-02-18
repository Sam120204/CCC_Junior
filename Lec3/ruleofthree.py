
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
    rule1 = input().split()
    rule2 = input().split()
    rule3 = input().split()
    
    d = {}
    d[rule1[0]] = (1, rule1[1])
    d[rule2[0]] = (2, rule2[1])
    d[rule3[0]] = (3, rule3[1])
    
    last_line = input().split()
    steps, start, end = int(last_line[0]), last_line[1], last_line[2]
    
    res = []
    dfs(start, end, d, res, [], steps)
    # found the solution
    if res:
        # we take the first one (any valid solution will work here)
        for line in res[0]:
            print(line)
J5_2019_Sol()
