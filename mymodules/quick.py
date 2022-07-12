## quick module

def replc_evry_othr(lst):
    '''replaces every other element st-indx-1 with everyother st-indx-0'''
    lst[1::2] = lst[::2]
    return lst