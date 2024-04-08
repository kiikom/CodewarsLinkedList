class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None:
        raise ValueError("Input list cannot be None")

    if head.next is None:
        raise ValueError("Input list should have more than one node for splitting")

    first_head = head
    second_head = head.next
    first_tail = first_head
    second_tail = second_head

    current = second_head.next
    is_first = True

    while current:
        if is_first:
            first_tail.next = current
            first_tail = first_tail.next
        else:
            second_tail.next = current
            second_tail = second_tail.next
        is_first = not is_first
        current = current.next

    first_tail.next = None
    second_tail.next = None

    return Context(first_head, second_head)

def print_linked_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")
