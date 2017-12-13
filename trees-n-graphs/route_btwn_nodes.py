class Node(object):

    def __init__(self, data, adj=None):
        self.data = data
        if adj is None:
            self.adj = set()
        else:
            self.adj = adj


class Graph(object):

    def are_connected(self, node1, node2):

        if node1 == node2:
            return True

        to_check = list(node1.adj)
        seen = {}

        while to_check:
            node = to_check.pop()
            if node not in seen:
                if node == node2:
                    return True
                else:
                    to_check.extend(list(node.adj))
                    seen.add(node)
        return False
