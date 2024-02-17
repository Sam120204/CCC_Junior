##Selection sort
# O(n^2)

def selection_sort(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):
        max_index = 0
        for j in range(0, i+1):
            if (lst[j] > lst[max_index]): 
                max_index = j

        temp = lst[i]
        lst[i] = lst[max_index]
        lst[max_index] = temp
    return lst
        

if __name__ == "__main__":
    l = [4,2,1,34,5342,2, -1, -2343]
    selection_sort(l)
    print(l)
            


