class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node {}>".format(self.data)

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def print_ll(self):

        current = self.head

        while current:
            print current
            current = current.next

def partition(llist, part):

    current = llist.head

    ll_left = LinkedList()
    ll_right = LinkedList()

    while current:
        print current
        if current.data < part:
            ll_left.add_node(current)
        else:
            ll_right.add_node(current)
        current = current.next

    ll_right.tail.next = None
    ll_left.add_node(ll_right.head)

    return ll_left

a = LinkedList()
a.add_node(Node(10))
a.add_node(Node(3))
a.add_node(Node(5))
a.add_node(Node(2))
b = partition(a, 5)
