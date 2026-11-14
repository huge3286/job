"""带路径重建的 Dijkstra。图使用非负边权。"""

from heapq import heappop, heappush
from itertools import count
from math import inf


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        """返回从 start 到 finish 的完整路径，不可达时返回空列表。"""
        distance = {start: 0}
        previous = {}
        sequence = count()
        queue = [(0, next(sequence), start)]
        while queue:
            current, _, node = heappop(queue)
            if current != distance[node]:
                continue
            if node == finish:
                path = [node]
                while node != start:
                    node = previous[node]
                    path.append(node)
                return path[::-1]

            for neighbor, weight in self.vertices.get(node, {}).items():
                if weight < 0:
                    raise ValueError("Dijkstra 要求边权非负")
                candidate = current + weight
                if candidate < distance.get(neighbor, inf):
                    distance[neighbor] = candidate
                    previous[neighbor] = node
                    heappush(queue, (candidate, next(sequence), neighbor))
        return []


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A", {"B": 7, "C": 8})
    graph.add_vertex("B", {"F": 2})
    graph.add_vertex("C", {"F": 6})
    graph.add_vertex("F", {"H": 3})
    assert graph.shortest_path("A", "H") == ["A", "B", "F", "H"]
    assert graph.shortest_path("H", "A") == []
    assert graph.shortest_path("A", "A") == ["A"]
    print(graph.shortest_path("A", "H"))
