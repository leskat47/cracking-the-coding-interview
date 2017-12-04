class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node {}>".format(self.data)

def remove_dups(ll):
    """
    >>> d = Node("berry")
    >>> c = Node("cherry", d)
    >>> b = Node("berry", c)
    >>> a = Node("apple", b)
    >>> remove_dups(a)
    >>> a.next
    <Node berry>
    >>> a.next.next
    <Node cherry>
    >>> a.next.next.next

    """

    current = ll
    all_data = set([current])

    while current.next:

        if current.next.data not in all_data:
            all_data.add(current.next.data)
        else:
            current.next = current.next.next
        if current.next:
            current = current.next
