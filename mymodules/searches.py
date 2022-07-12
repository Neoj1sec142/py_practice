
def find_index(list, target):
    '''Find the index of a value in sequence'''
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1


def find_tar(list, tar):
    '''Find the target value in sequence'''
    for val in list:
        if val == tar:
            return val
    return -1

def find_pair(values, total):
    '''Finds a pair of values in a list that
         equals a given total target'''
    known = set()
    for value in values:
        if total - value in known:
            return value, total - value
        known.add(value)

def remove_lessrel(text):
    '''Removes Words with Less than 3 characters from a paragraph variable'''
    w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]
    return w