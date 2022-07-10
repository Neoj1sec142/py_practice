
def find_index(list, target):
    '''Find the index of a value in sequence'''
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1


def find_target(list, target):
    '''Find the target value in sequence'''
    for value in list:
        if value == target:
            return value
    return -1

def find_pair(values, total):
    '''Finds a pair of values in a list that
         equals a given total target'''
    known = set()
    for value in values:
        if total - value in known:
            return value, total - value
        known.add(value)
