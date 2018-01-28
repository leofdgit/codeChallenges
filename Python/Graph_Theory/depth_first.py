def dfs(ug,start):
  '''
  ug is an undirected graph whose edges do not have associated edges.
  '''
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        for n in ug.neighbours[node]:
            if n not in visited:
                stack.append(n)
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
G.addNeighbours(4,6)
print(dfs(G,0))
'''
