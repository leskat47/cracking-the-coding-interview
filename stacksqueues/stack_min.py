
class Stack(object):
    """ Stack class with find minimum function. Brute force, which could be
        changed if we want the location of the item or just the value
    """

    def __init__(self):
        self.stack = []
        self.smallest= None
        self.min_location = None

    def push(self, item):
        self.stack.append(item)
        if item < self.smallest or not self.min:
            self.smallest= item
            self.min_location = len(self.stack) - 1

    def pop(self):
        popped = self.stack.pop()
        if self.min_location == len(self.stack) - 1:
            self.smallest= self.stack[0]
            for idx, item in enumerate(self.stack):
                if item < new_min:
                    self.smallest= item
                    self.min_location = idx
        return popped

    def find_min(self):
        return smallest


# /////////////////////////////////////////////////////////////////////////

class StackNode(object):

    def __init__(self, value, next=None, next_lowest=None):
        self.value = value
        self.next = next
        self.next_lowest = next_lowest

    def __repr__(self):
        return "<Node: {}>".format(self.value)

class StackMin(object):
    """
        Stack with a minimum method. Creates a secondary linked list by having
        nodes track their next-lowest value
    """

    def __init__(self):
        self.top = None
        self.minimum = None

    def push(self, new_data):
        new_node = StackNode(new_data)

        if not self.top:
            print "No top"
            self.minimum = new_node
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

            if self.top.value < self.minimum.value:
                self.top.next_lowest = self.minimum
                self.minimum = self.top

    def pop(self):

        if not self.top:
            return None

        popped = self.top

        if popped == self.minimum:
            self.minimum = self.top.next_lowest

        self.top = self.top.next
        return popped

    def find_minimum(self):
        return self.minimum

s_m = StackMin()
s_m.push(5)
print "minimum ", s_m.find_minimum()
s_m.push(4)
print "minimum ", s_m.find_minimum()
s_m.push(7)
print "minimum ", s_m.find_minimum()
s_m.push(3)

print s_m.find_minimum()
print s_m.pop()
print s_m.find_minimum()
