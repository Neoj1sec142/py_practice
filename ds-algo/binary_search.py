
def binary_search(list, target):
    first = 0
    last = len(list) -1
    while first <= last:
        mid = (first + last)//2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

## Verification
def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")
nums = range(0,1000)
res = binary_search(nums, 127)
verify(res)