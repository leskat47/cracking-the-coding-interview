class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "<Node {}>".format(self.data)

# ///////////////////////////////////////////////////////
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

# ///////////////////////////////////////////////////////

def k_to_last(a, k):
    """ Slightly optimized return k from the end of linked list"""

    half = a
    full = a

    length = 1

    while full.next and full.next.next:
        half = half.next
        full = full.next.next
        length += 2

    if full.next:
        length += 1

    if k <= length / 2:
        count = length / 2 - k
        for i in range(count + 1):
            half = half.next
        return half
    else:
        count = length - k
        current = a
        for i in range(count):
            current = current.next
        return current

f = Node("fresa")
e = Node("elderberry", f)
d = Node("durian", e)
c = Node("cherry", d)
b = Node("berry", c)
a = Node("apple", b)
print binary_k_to_last(a, 3)


# def count_to_end(current, n):
#     """Are we n nodes from the end"""
#
#     if n == 0 and not current:
#         return True
