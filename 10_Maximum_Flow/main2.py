from tabulate import tabulate
from openpyxl import Workbook

class Graph:
    def __init__(self, graph, nodes):
        self.graph = graph
        self.nodes = nodes

    def bfs(self, s, t, parent):
        # Остальной код остается без изменений

    def ford_fulkerson(self, source, sink):
        # Остальной код остается без изменений

    def generate_excel(self, max_flow):
        wb = Workbook()
        ws = wb.active

        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                ws.cell(row=i+1, column=j+1).value = self.graph[i][j]

        # Запись максимального потока
        ws.append(["Максимальный поток:", max_flow])

        return wb


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

# Создание Excel-файла и запись таблиц в него
wb = g.generate_excel(max_flow)
wb.save("graph_tables.xlsx")
