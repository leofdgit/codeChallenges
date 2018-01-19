
class node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None    

def lca(root , v1 , v2):
    '''
    Returns the lowest common ancestor of v1 and v2 in the tree.
    This function assumes that v1 and v2 are both in the tree.
    '''
    if root.data < v1 and root.data < v2:
        return lca(root.right,v1,v2)
    elif root.data > v1 and root.data > v2:
        return lca(root.left,v1,v2)
    else:
        return root.data
        
'''
Test Cases:

#create test tree 1:
root = node(5)
a,b = node(3), node(7)
root.left, root.right = a,b
c,d = node(1), node(4)
a.left, a.right = c,d
e,f = node(6), node(9)
b.left, b.right = e,f

print(lca(root, 9,1))

#create test tree 2:
root = node(5)
a,b = node(3), node(7)
root.left, root.right = a,b
c,d = node(1), node(4)
a.left, a.right = c,d
e,f = node(6), node(2)
b.left, b.right = e,f

print(lca(root,1,4))
'''
