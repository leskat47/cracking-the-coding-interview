class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.lchild = left
        self.rchild = right

def build_bst(items):
    """ From a sorted list make a balanced binary search tree.

        >>> lst = [ 1, 2, 3, 4, 5, 6, 7]
        >>> l = build_bst(lst)
        >>> l.data
        4
        >>> l.lchild.lchild.data
        1
        >>> l.rchild.data
        6

    """


    if len(items) == 1:
        return Node(items[0])
    elif not items:
        return None

    mid = len(items)/2

    left_branch = items[:mid]
    right_branch = items[mid + 1:]

    lchild = build_bst(left_branch)
    rchild = build_bst(right_branch)

    node = Node(items[mid], lchild, rchild)

    return node
