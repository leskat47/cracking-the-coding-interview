class Node(object):

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.lchild = left
        self.rchild = right
        self.parent = parent


    def get_next(self):
        """ Find next node of an in-order traversal

        >>> n1 = Node("1")
        >>> n7 = Node("7")
        >>> n5 = Node("5", n1, n7)
        >>> n1.parent = n5
        >>> n7.parent = n5
        >>> n15 = Node("15", None, None)
        >>> n30 = Node("30", None, None)
        >>> n20 = Node("20", n15, n30)
        >>> n15.parent = n20
        >>> n30.parent = n20
        >>> n10 = Node("10", n5, n20)
        >>> n5.parent = n10
        >>> n20.parent = n10

        >>> assert n5.get_next() == n7, 'has a right child'
        >>> assert n7.get_next() == n10, 'called on right child of left half'
        >>> assert n1.get_next() == n5, 'left leaf node'
        >>> assert n30.get_next() == None, 'last possible node'

        """
        # return right child_left
        if self.rchild:
            return self.rchild

        # if there is no right child
        # if it is the left child, return the parent
        if self.parent and self.parent.lchild == self:
            return self.parent

        # it must be a right child, return the first parent of a left child
        current = self
        while current.parent:
            if current.parent.lchild == current:
            # is an ancestor ever a left child?
                return current.parent
            current = current.parent

        # we've reached the root, return
        return None
