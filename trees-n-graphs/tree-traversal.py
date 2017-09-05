class Node(object):
    
    def __init__(self, data, left, right):
        self.data = data
        self.child_left = left
        self.child_right = right
        
def pre_order_traversal(node):
    if node:
        print node.data
        pre_order_traversal(node.child_left)
        pre_order_traversal(node.child_right)
        
def post_order_traversal(node):
    if node: 
        post_order_traversal(node.child_left)
        post_order_traversal(node.child_right)
        print node.data

def in_order_traversal(node):
    if node:
        in_order_traversal(node.child_left)
        print node.data
        in_order_traversal(node.child_right)


class Tree(object):
    
    def __init__(self, root):
        self.root = root
        


# In[102]:


n1 = Node("1", None, None)
n7 = Node("7", None, None)
n5 = Node("5", n1, n7)
n15 = Node("15", None, None)
n30 = Node("30", None, None)
n20 = Node("20", n15, n30)
n10 = Node("10", n5, n20)


# In[103]:


t = Tree(n10)


# In[49]:


t.root


print "pre order"
pre_order_traversal(t.root)


# In[104]:

print "post order"
post_order_traversal(t.root)



print "in order"
in_order_traversal(t.root)




