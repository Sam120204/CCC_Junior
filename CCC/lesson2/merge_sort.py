##Merge sort
# O(nlogn)

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        leftlst = lst[:mid] #colon to mid
        rightlst =lst[mid:]
        
        merge_sort(leftlst)
        merge_sort(rightlst)
        
        i = j = k = 0
        # Copy data to temp arrays leftlst[] and rightlst[]
        while i < len(leftlst) and j < len(rightlst):
            if leftlst[i] < rightlst[j]:
                lst[k] = leftlst[i]
                i += 1
            else:
                lst[k] = rightlst[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(leftlst):
            lst[k] = leftlst[i]
            i += 1
            k += 1

        while j < len(rightlst):
            lst[k] = rightlst[j]
            j += 1
            k += 1
        

        

if __name__ == "__main__":
    l = [4,2,1,34,5342,2, -1, -2343]
    merge_sort(l)
    print(l)
            


