
def merge_sort(list):
    '''Sorts a list in ascending order --
    returns a new sorted list
    Divide: find the midpoint of list and divide into sub-lists
    Conquer: recursively sort the sub-lists created in prev
    Combine: Merge the sorted sub-lists
    overall of whole shabang is O(n log n) runtime'''
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    # print("%s %s"%(left, right))
    return merge(left, right)

def split(list):
    '''divide the unsorted list at midpoint into sub-lists
    returns sub-lists left to right
    takes overall O(log n) time'''
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right

def merge(left, right):
    '''merges 2 lists or arrays sorting them in the process
    returns a new merged list
    runs in overall linear time O(n)'''
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # print("%s - %s" % (left, right))
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
            print()

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])


### Testing
alst = [54, 26, 93, 17, 77, 31, 20, 30, 10, 43]
l = merge_sort(alst)
print(verify_sorted(alst))
print(verify_sorted(l))
print(l)