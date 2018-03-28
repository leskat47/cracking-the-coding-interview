class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def print_ll(self):
        current = self
        while current:
            print current
            current = current.next

    def __repr__(self):
        return "<Node {}>".format(self.data)

def del_node(node):
    """ Given a node, remove it from a linked list

        >>> d = Node("durian")
        >>> c = Node("cherry", d)
        >>> b = Node("berry", c)
        >>> a = Node("apple", b)
        >>> del_node(c)
        >>> a.print_ll()
        <Node apple>
        <Node berry>
        <Node durian>

    """

    val = node.data

    while node.next.next:
        node.data = node.next.data
        node = node.next

    node.data = node.next.data
    node.next = None
