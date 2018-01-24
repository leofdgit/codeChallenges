class MinHeap():
    '''
    Implementation of a min heap. A min heap is a binary tree such that the children of any node n have values less than that of n.
    This implementation is based on that of Gayle Laakmann McDowell, as seen on HackerRank.
    '''
    def __init__(self):
        self.nodes = []
        self.len = 0
    def swapValues(self,a,b):
        self.nodes[a], self.nodes[b] = self.nodes[b], self.nodes[a]
    def addNode(self,val):
        self.nodes.append(val)
        self.len += 1
        idx = self.len-1
        while self.hasParent(idx):
            if self.getParent(idx) > self.nodes[idx]:
                self.swapValues(idx, self.getParentIndex(idx))
                idx = self.getParentIndex(idx)
            else:
                break
    def deleteTop(self):
        if self.len == 0:
            raise IndexError('No elements to delete.')
        elif self.len == 1:
            self.len -= 1
            self.nodes = []
        else:
            self.swapValues(0,-1)
            self.nodes.pop()
            self.len -= 1
            idx = 0
            while self.hasLeftChild(idx):
                c = self.getLeftChildIndex(idx)
                if self.hasRightChild(idx):
                    if self.getRightChild(idx) < self.getLeftChild(idx):
                        c = self.getRightChildIndex(idx)
                if self.nodes[idx] > self.nodes[c]:
                    self.swapValues(idx,c)
                    idx = c
                else:
                    break

    def getParent(self,node):
        return self.nodes[(node-1)//2]
    def getLeftChild(self,node):
        return self.nodes[(node*2) + 1]
    def getRightChild(self,node):
        return self.nodes[(node*2) + 2]
    def getLeftChildIndex(self,node):
        return node*2 + 1
    def getRightChildIndex(self,node):
        return node*2 + 2
    def getParentIndex(self,node):
        return (node-1)//2
    def hasParent(self,node):
        if node == 0:
            return False
        else:
            return True
    def hasLeftChild(self,node):
        if 2*node + 1 < len(self.nodes):
            return True
        else:
            return False
    def hasRightChild(self,node):
        if 2*node + 2 < len(self.nodes):
            return True
        else:
            return False
'''
#Test Heap.
M = MinHeap()
M.addNode(2)
M.addNode(3)
M.addNode(1)
M.addNode(5)
M.addNode(7)
M.addNode(77)
M.addNode(777)
M.addNode(9)
M.addNode(10)
M.deleteTop()
print(M.nodes)
'''
