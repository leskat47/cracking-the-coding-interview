
# coding: utf-8

# In[38]:


class Node(object):
    """Node in a tree."""

    def __init__(self, data, child_left=None, child_right=None):
        self.data = data
        self.child_left = child_left
        self.child_right = child_right

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data


# In[2]:


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root


# In[39]:


resume = Node("resume.txt")
recipes = Node("recipes.txt")
jane = Node("jane/", resume, recipes)
server = Node("server.py")
jessica = Node("jessica/", server)
users = Node("Users/", jane, jessica)
root = Node("/", users)

tree = Tree(root)


# In[45]:


def find_common_ancestor(root, node1, node2):
    if not in_subtree(root, node1) or not in_subtree(root, node2):
        return
    return ancestor_helper(root, node1, node2)


def ancestor_helper(root, node1, node2):
    if not root or root == node1 or root == node2:
        return root
    onleft1 = in_subtree(root.child_left, node1)
    onleft2 = in_subtree(root.child_left, node2)
    if (onleft1 != onleft2):
        return root
    if onleft1:
        return ancestor_helper(root.child_left, node1, node2)
    else:
        return ancestor_helper(root.child_right, node1, node2)
    
def in_subtree(root, node):
    if not root:
        return False
    if root == node:
        return True
    return in_subtree(root.child_left, node) or in_subtree(root.child_right, node)
        


# In[46]:


print find_common_ancestor(root, resume, recipes)


# In[ ]:




