# runtime: O(logn)

def bs(lst, val):
    start, end = 0, len(lst)
    while (start < end):
        mid = (start + end) // 2
        if lst[mid] == val: return True
        elif lst[mid] < val: start = mid + 1
        else: end = mid
    return False

if __name__ == "__main__":
    assert bs([1,2,3,4,5,6], 3) == True, "error"
    assert bs([1,2,3,4,5,6], 7) == False, "error"
    print("test passed")
    