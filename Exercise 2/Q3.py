
from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)


    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


def reachable(graph, value):
    list = graph.graph[value]
    list.insert(0,value)
    for x,y in graph.graph.items():
        if value in y and value != x:
            list.append(x)

    return list

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge('a', 'b')
g.addEdge('a', 'c')
g.addEdge('b', 'd')
g.addEdge('c','')
g.addEdge('d', 'a')
g.addEdge('e', 'd')


print("a reachable:")
print(reachable(g,'a'))


