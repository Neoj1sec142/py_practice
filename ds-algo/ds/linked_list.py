class Node:
    '''object for storing a single node of a linked list
    models 2 attributes, data and link to the next node in list'''
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>"%self.data

class LinkedList:
    '''Singly Linked List'''
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def size(self):
        '''returns number of nodes in list with linear time'''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    def add(self, data):
        '''adds a new node containing data at the head of the list
            this option takes constant time which is best case'''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        '''returns a str representation of the list O(n) time'''
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]"%current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]"%current.data)
            else:
                nodes.append("[%s]"%current.data)
            current = current.next_node
        return '-> '.join(nodes)