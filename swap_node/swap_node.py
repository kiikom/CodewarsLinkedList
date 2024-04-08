from preloaded import Node

def swap_pairs(head):
    if head is None:
        return None
    if head.next is None:
        return head
    new = Node()
    new.next = head
    prev = new
    while prev.next and prev.next.next:
        first_node = prev.next
        second_node = prev.next.next
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        prev = first_node
    return new.next