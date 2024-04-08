def loop_size(node):
    count = 1
    first = node.next
    second = node.next.next
    while first!= second:
        first = first.next
        second = second.next.next
    second = first.next
    while first!= second:
        count = count+1
        second = second.next
    return count