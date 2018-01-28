class UGraph():
  '''
  Class for an undirected graph without edge weights.
  '''
    def __init__(self):
        self.neighbours = defaultdict(list)
    def addNeighbours(self,a,b):
        self.neighbours[a].append(b)
        self.neighbours[b].append(a)


def bfs(ug,start):
  '''
  ug is an undirected graph whose edges do not have weights associated with them.
  start is the node from which the breadth-first search will start from. 
  '''
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
        for n in ug.neighbours[node]:
            if n not in visited:
                queue.append(n)
    return visited
    
'''
#test
G = UGraph()
G.addNeighbours(0,1)
G.addNeighbours(0,2)
G.addNeighbours(2,3)
G.addNeighbours(3,4)
G.addNeighbours(1,5)
G.addNeighbours(5,6)
print(bfs(G,0))
'''
