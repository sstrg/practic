from collections import deque

class Graph:
    def __init__(self, n):
        self.g = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def bfs(self, start):
        visited = [False] * len(self.g)
        order = []
        q = deque([start])
        visited[start] = True

        while q:
            v = q.popleft()
            order.append(v)
            for to in self.g[v]:
                if not visited[to]:
                    visited[to] = True
                    q.append(to)
        return order

    def dfs(self, start):
        visited = [False] * len(self.g)
        order = []

        def go(v):
            visited[v] = True
            order.append(v)
            for to in self.g[v]:
                if not visited[to]:
                    go(to)

        go(start)
        return order

    def shortest_path(self, start, end):
        visited = [False] * len(self.g)
        parent = [-1] * len(self.g)
        q = deque([start])
        visited[start] = True

        while q:
            v = q.popleft()
            if v == end:
                break
            for to in self.g[v]:
                if not visited[to]:
                    visited[to] = True
                    parent[to] = v
                    q.append(to)

        if not visited[end]:
            return []

        path = []
        cur = end
        while cur != -1:
            path.append(cur)
            cur = parent[cur]

        return path[::-1]


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)

print(g.bfs(0))
print(g.dfs(0))
print(g.shortest_path(0, 5))