class Graph:
    def init(self, V):
        self.V = V  # number of vertices
        self.adj = {}  # adjacent lists

        # Initialize adjacency lists
        for i in range(V):
            self.adj[i] = []

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.adj[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self):
        visited = [False] * self.V
        #Transversal at Node 0
        self.DFSUtil(0, visited)

#Test Case
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 3)
g.add_edge(3, 5)

g.DFS()