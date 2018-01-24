from collections import defaultdict

class graph():
    '''
    The graph structure here has weights associated with each edge.
    
    A graph with N nodes should have nodes labelled 0,1,...,N-1, else the algorithm will fail. Caution must be taken to
    ensure this restriction is adhered to. The implementation could be improved to avoid the user being responsible for this.
    '''
    def __init__(self):
        self.neighbours = defaultdict(list)
        self.distances = defaultdict(int)

    def add_neighbours(self, a,b, d):
        self.neighbours[a].append(b)
        self.neighbours[b].append(a)
        self.distances[(a,b)] = d
        self.distances[(b,a)] = d



def dijkstra(graph, start):
    '''
    This algorithm returns the shortest paths (with distances) from start to each other node in the graph.
    '''
    not_visited = set([i for i in graph.neighbours]) #assume that all graphs have nodes labelled 0, 1, ..., n-1.
    distances = {}
    distances[start] = 0
    path = {}
    while(not_visited):

        #First: pick the unexplored node at minimum distance from an explored node.
        #If no node has been explored, then this the start node is chosen.
        #Can't take a node that is not a neighbour of an already-visited node.
        taken_node = None
        if len(not_visited) == len(graph.neighbours):
            taken_node = start
        else:
            for node in not_visited:
                if node not in distances:
                    continue
                else:
                    if taken_node == None:
                        taken_node = node
                        continue
                    if distances[node] < distances[taken_node]:
                        taken_node = node

        try:
            not_visited.remove(taken_node)
            current_dist = distances[taken_node]
        except KeyError:
             print('Graph is not connected.')
             return

        #now we have closest neighbour to known region, look at its neighbours and:
        #if distance to a node not in set, add current distance + distance from taken_node to distances
        #if distance to a node in set, replace if current dist. + dist. from taken_node less than value in set
        for neigh in graph.neighbours[taken_node]:
            combined_dist = current_dist + graph.distances[(taken_node,neigh)]
            if neigh not in distances:
                distances[neigh] = combined_dist
                path[neigh] = taken_node
            else:
                if distances[neigh] > combined_dist:
                    distances[neigh] = combined_dist
                    path[neigh] = taken_node
    return distances, path

'''
#Test.
T = graph()
T.add_neighbours(0,1,5)
T.add_neighbours(0,2,5)
T.add_neighbours(1,3,5)
T.add_neighbours(3,4,5)
T.add_neighbours(4,0,5)
print(dijkstra(T,0))
'''
