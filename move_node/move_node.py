class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError("error should be thrown when source list is empty")
    else:
        next_source = source.next
        source.next = dest
        return Context(next_source, source)


