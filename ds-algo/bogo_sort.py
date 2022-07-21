import random

numbers = [4,6,1,7,8,3]

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attmps = 0
    while not is_sorted(values):
        random.shuffle(values)
        attmps += 1
        print(attmps)
    return values

# print(bogo_sort(numbers))
