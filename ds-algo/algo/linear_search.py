


def linear_search(list, target):
    '''returns the index position of target, else None'''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

## Verification
def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")
lst = [1,2,3,4,5,6,7,8,9]
res = linear_search(lst, 5)
verify(res)