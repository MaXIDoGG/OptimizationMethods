from tabulate import tabulate
from collections import deque


class Graph:
    def __init__(self, graph, nodes):
        self.graph = graph
        self.nodes = nodes

    def bfs(self, s, t, parent):
        visited = [False] * len(self.graph)
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v in range(len(self.graph)):
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * len(self.graph)
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            print("Распределение потока:")
            headers = [""] + [f"P{i}" for i in self.nodes]
            rows = [[f"P{i}"] + row for i, row in enumerate(self.graph)]
            print(tabulate(rows, headers=headers, tablefmt="grid"))
            print("Поток на этом этапе:", path_flow)
            print("")

        return max_flow


# Пример использования
graph = [
    [0, 15, 16, 18, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 6, 9, 0, 0],
    [0, 0, 0, 0, 8, 5, 6, 0, 0],
    [0, 0, 0, 0, 11, 12, 0, 0, 0],
    [0, 7, 6, 12, 0, 6, 0, 0, 13],
    [0, 7, 6, 9, 6, 0, 0, 5, 11],
    [0, 7, 5, 0, 0, 0, 0, 10, 12],
    [0, 0, 0, 0, 0, 5, 8, 0, 14],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

nodes = [i for i in range(len(graph))]

g = Graph(graph, nodes)
source = 0
sink = 8
max_flow = g.ford_fulkerson(source, sink)
print(f"Максимальный поток из вершины {source} в вершину {sink} равен {max_flow}")
