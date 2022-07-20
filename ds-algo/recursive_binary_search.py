
# This is a recursive implementation of the binary search
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list)//2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid], target)

# the return is important so you can eventually end the while loop
# hence instructing the program to return the output value to itself
# works on the problem until it has a good answer
# python has a maximum recursion depth

## Verification
def verify(result):
    print(f'Target found: {result}')

nums = range(0,1000)
res1 = recursive_binary_search(nums, 127)
verify(res1)

res2 = recursive_binary_search(nums, 10011)
verify(res2)