from collections import defaultdict
import functools

class Solution():
    def makeConnected(self, n, connections):
        if(len(connections) < n-1):
            return -1
        # number of isolated clusters are 0
        total_clusters = 0
        # if not smaller than n-1 create the adjacency graph
        self.createAdjacencyGraph(connections)
        # and implement the dfs on the graph
        # for vertex in all vertices
        for v in range(n):
            if v not in self.visited:
                total_clusters += 1
                self.dfs(v)
        return total_clusters -1      

    def createAdjacencyGraph(self, connections):
        self.graph, self.visited = defaultdict(list), set()
        for x, y in connections:
            self.graph[x].append(y)
            self.graph[y].append(x)
                      
    def dfs(self, v):
        # add v to the visited set so we dont go in a cyclical loop
        self.visited.add(v)
        # for every node that is not visited, put them in the dfs cycle
        for i in self.graph[v]:
            if i not in self.visited:
                self.dfs(i)  
        