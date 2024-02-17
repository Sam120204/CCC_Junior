def Magical_Magnetic_Marbles(n, k, slots):
    for i in range(n):
        if i > 0:
            if slots[i] and slots[i-1]:
                slots[i-1] = 0

    groups, amount, ones = [], 0, 0
    for i in range(n):
        if slots[i]: # slot = 1
            if ones: # other
                ones += 1
                groups.append(amount)
            else: # first slot
                ones += 1
            amount = 0
        else: # slot = 0
            amount += 1

    if groups:
        groups = sorted(groups)
        for group in groups:
            if group <= k:
                ones -= 1
                k -= group
            else: break
    else:
        if k: ones = 1
        else: ones = 0
    return ones

if __name__ == "__main__":
    n, k = map(int, input().split(" "))
    slots = [int(i) for i in input()]
    print(Magical_Magnetic_Marbles(n, k, slots))
