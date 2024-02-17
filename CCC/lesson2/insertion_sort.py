##Insertion sort
# O(n^2)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        cur = lst[i]
        pos = i
        while pos > 0 and lst[pos-1] > cur:
            lst[pos] = lst[pos-1]
            pos-=1
            
        lst[pos] = cur
    return lst
        

if __name__ == "__main__":
    l = [4,2,1,34,5342,2, -1, -2343]
    insertion_sort(l)
    print(l)
            


