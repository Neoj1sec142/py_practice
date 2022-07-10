#import main as mn
import sys
sys.path.append('/Users/neo/.mine/practice/python/py_practice/mymodules')
from quick1 import find_target as fi

# from main import find_index as fi, test as t
courses = ['Python', 'Java', 'PHP', 'Perl', 'JS']

print(fi(courses, 'PHP'))
# print(t)
# print(sys.path) #= prints paths python searches for modules
