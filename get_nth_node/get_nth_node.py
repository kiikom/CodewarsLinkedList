from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise ValueError("None linked list should throw error.")
    if index < 0:
        raise ValueError("Invalid index value should throw error.")
    
    current = node
    count = 0
    while current:
        if count == index:
            return current
        count += 1
        current = current.next
    
    raise ValueError("Invalid index value should throw error.")
