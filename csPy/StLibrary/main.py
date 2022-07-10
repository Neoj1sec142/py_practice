# 8. Import Modules and the Standard Library
# this will be a module that will have a funciton that will take 
# a list of values and search for a targets index

print('Imported My Module....')

test = 'Test String'

def find_index(list, target):
    '''Find the index of a value in sequence'''
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1

