x = [input().strip().split() for i in range(int(input()))]
y = [input().strip().split() for i in range(int(input()))]
groups = {}

for group_number in range(int(input())):
    a, b, c = input().strip().split()
    groups[a], groups[b], groups[c] = group_number, group_number, group_number

violations = 0

for a, b in x:
    violations += groups[a] != groups[b]

for a, b in y:
    violations += groups[a] == groups[b]

print(violations)