def linked_list_from_string(s):
    lst = s.split('->')[-2::-1]
    node = None
    for elem in lst:
        node = Node(int(elem), node)
    return node