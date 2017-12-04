class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node {}>".format(self.data)


def find_length(a):

    count = 1
    current = a

    while current.next:
        count += 1
        current = current.next

    return count

def get_k_to_last(a, k):

    idx = 1

    length = find_length(a)

    if length < k:
        return None

    location = length - k
    current = a

    while location:
        current = current.next
        location -= 1

    return current

d = Node("durian")
c = Node("cherry", d)
b = Node("berry", c)
a = Node("apple", b)
print get_k_to_last(a, 2)

# def count_to_end(current, n):
#     """Are we n nodes from the end"""
#
#     if n == 0 and not current:
#         return True

# binary searsh - use 2 runners to determine lengthe and midpoint
