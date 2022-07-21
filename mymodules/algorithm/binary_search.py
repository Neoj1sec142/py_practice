def binary_search(vals, t):
    fst = 0
    lst = len(vals) -1
    while fst <= lst:
        mid = (fst + lst)//2
        if vals[mid] == t:
            return mid
        elif vals[mid] < t:
            fst = mid + 1
        else:
            lst = mid - 1
    return None