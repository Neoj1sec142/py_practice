class Node:
    '''object for storing a single node of a linked list
    models 2 attributes, data and link to the next node in list'''
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>"%self.data