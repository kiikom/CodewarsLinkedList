class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    if node is None:
        return "None"
    current = node
    result = ''
    while current:
        result += str(current.data)
        if current.next:
            result += ' -> '
        current = current.next
    result += ' -> None'
    return result
