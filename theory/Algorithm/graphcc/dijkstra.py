import heapq
import sys


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {}  # 统计出发点到当前节点的距离
        previous = {}  # 当前最优路径的上一个节点
        nodes = []  # 优先队列保存所有的路径

        # 把所有结点都放入优先队列 除了初始节点之外 距离都初始化为无穷大
        for vertex in self.vertices:
            if vertex == start:  # 初始节点的距离是0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])  # 类似之前的搜索算法 push [距离, 节点]
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
            previous[vertex] = None

        while nodes:
            smallest = heapq.heappop(nodes)[1]  # 弹出当前与起点距离最小的节点
            if smallest == finish:  # 如果已经遍历到 输出结果
                path = []
                while previous[smallest]:  # 往上回溯到起始节点
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == sys.maxsize:  # All remaining vertices are inaccessible from source
                break

            for neighbor in self.vertices[smallest]:  # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor]  # Alternative path distance
                if alt < distances[neighbor]:  # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)

        print("nice")
        return distances

    def __str__(self):
        return str(self.vertices)


if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A", {"B": 7, "C": 8})
    g.add_vertex("B", {"A": 7, "F": 2})
    g.add_vertex("C", {"A": 8, "F": 6, "G": 4})
    g.add_vertex("D", {"F": 8})
    g.add_vertex("E", {"H": 1})
    g.add_vertex("F", {"B": 2, "C": 6, "D": 8, "G": 9, "H": 3})
    g.add_vertex("G", {"C": 4, "F": 9})
    g.add_vertex("H", {"E": 1, "F": 3})
    print(g.shortest_path("A", "H"))
