# finds the index of a target value in a list
def find_index(list, target):
    '''Find the index of a value in sequence'''
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1

# finds a target in a list if not returns -1
def find_target(list, target):
    '''Find the target value in sequence'''
    for value in list:
        if value == target:
            return value
    return -1