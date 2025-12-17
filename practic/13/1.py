#матрицв смежности
class AdjacencyMatrixGraph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, w=1):
        self.matrix[u][v] = w
        self.matrix[v][u] = w

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def has_edge(self, u, v):
        return self.matrix[u][v] != 0


g = AdjacencyMatrixGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)

print(g.matrix)
print(g.has_edge(0, 1))
print(g.has_edge(2, 3))



#список смлкности
class AdjacencyListGraph:
    def __init__(self, n):
        self.graph = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def neighbors(self, v):
        return self.graph[v]


g = AdjacencyListGraph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)

print(g.graph)
print(g.neighbors(0))