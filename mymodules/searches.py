# searches module

def find_index(lst, target):
    '''Find the index of a value in sequence'''
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1


def find_tar(lst, tar):
    '''Find the target value in sequence'''
    for val in lst:
        if val == tar:
            return val
    return -1

def find_pair_sum(vals, tot):
    '''Finds a pair of values in a list that
         equals a given total target'''
    known = set()
    for val in vals:
        if tot - val in known:
            return val, tot - val
        return known.add(val)

def remove_lessrel(text):
    '''Removes Words with Less than 3 characters from a paragraph variable'''
    w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]
    return w

def sub_search(txt, tar):
    '''returns true if substring carries target'''
    mark = map(lambda s: (True, s) if str(tar) in s else (False, s), txt)
    return(list(mark))

def find_context(to_search, tar):
    '''returns the context 18 char radius of target search (multiline str search)'''
    find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1
    return(find(to_search, str(tar)))

def find_short(s):
    '''Finds Shortest word in a string'''
    return min(len(a) for a in s.split())

