
nums = [3,9,10,6,8,1,2,14,7,4]

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values:
        if value in values[1:]:
            less_than_pivot.append(value)

sorted_numbers = quicksort(nums)
print(sorted_numbers)
