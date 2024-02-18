p = input().split()
print(p)
n = int(p[0])
k = int(p[1])
slots = [int(i) for i in input()]

for i in range(n):
    if i > 0:
        if slots[i] and slots[i-1]:
            slots[i-1] = 0
#[0,1,1,1] -> [0,0,0,1]

groups, amount, ones = [], 0, 0

# 6 1
# 010111 -> 010001

for i in range(n):
    if slots[i]: # slot[i] = 1
        if ones:
            ones += 1
            groups.append(amount)
        
        else:
            ones += 1
        amount = 0
    else: # slots[i] = 0
        amount += 1

#groups = [3]

groups.sort()
if groups:
    for group in groups:
        if group <= k:
            k -= group
            ones -= 1
        else:
            break
else:
    if k: ones = 1
    else: ones = 0

print(ones)
