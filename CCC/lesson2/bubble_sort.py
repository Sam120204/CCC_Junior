##Bubble sort
# O(n^2)

def bubble_sort(lst):
    n = len(lst)
    for l in range(n - 1, 0, -1):
        for j in range(0, l):
            if lst[j] > lst[j+1]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp
    return lst

if __name__ == "__main__":
    l = [4,2,1,34,5342,2, -1, -2343]
    bubble_sort(l)
    print(l)
            


