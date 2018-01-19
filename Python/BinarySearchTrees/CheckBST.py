""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    '''
    Check if a binary tree is a binary search tree.
    
    The function works as follows: root is given as input. Then a queue of tuples is created. The queue of tuples represents nodes in
    subtrees connected to the root.
    
    The tuples are of length three. The leftmost element of the tuple is the node in the current subtree of minimum value.
    The rightmost element of the tuple is the node in the current subtree of maximum value. The middle node is the current
    node being investigated.
    
    The idea is that every node in every subtree tree has value less than the largest value in the subtree, and greater than
    the smallest value in the subtree.
    '''
    initial_l = node(float('-inf'))
    initial_r = node(float('inf'))
    queue = [(initial_l, root, initial_r)]
    while queue:
        l, m, r = queue.pop(0)
        if l.data < m.data < r.data:
            if m.left:
                queue.append((l,m.left,m))
            if m.right:
                queue.append((m,m.right,r))
        else:
            return False
    return True
        
