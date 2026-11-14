#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>

class Graph {
public:
    void add_vertex(char node, const std::unordered_map<char, int>& edges) {
        vertices[node] = edges;
    }

    // Return the complete path, or an empty vector if finish is unreachable.
    std::vector<char> shortest_path(char start, char finish) const {
        using Candidate = std::pair<long long, char>;
        std::priority_queue<Candidate, std::vector<Candidate>, std::greater<Candidate>> queue;
        std::unordered_map<char, long long> distances{{start, 0}};
        std::unordered_map<char, char> previous;
        queue.emplace(0, start);
        while (!queue.empty()) {
            auto [distance, node] = queue.top();
            queue.pop();
            if (distance != distances.at(node)) {
                continue;
            }
            if (node == finish) {
                std::vector<char> path{node};
                while (node != start) {
                    node = previous.at(node);
                    path.push_back(node);
                }
                std::reverse(path.begin(), path.end());
                return path;
            }
            auto edges = vertices.find(node);
            if (edges == vertices.end()) {
                continue;
            }
            for (auto [neighbor, weight] : edges->second) {
                if (weight < 0) {
                    throw std::invalid_argument("Dijkstra requires nonnegative weights");
                }
                auto candidate = distance + weight;
                auto known = distances.find(neighbor);
                if (known == distances.end() || candidate < known->second) {
                    distances[neighbor] = candidate;
                    previous[neighbor] = node;
                    queue.emplace(candidate, neighbor);
                }
            }
        }
        return {};
    }

private:
    std::unordered_map<char, std::unordered_map<char, int>> vertices;
};

int main() {
    Graph graph;
    graph.add_vertex('A', {{'B', 7}, {'C', 8}});
    graph.add_vertex('B', {{'F', 2}});
    graph.add_vertex('C', {{'F', 6}});
    graph.add_vertex('F', {{'H', 3}});
    auto path = graph.shortest_path('A', 'H');
    if (path != std::vector<char>{'A', 'B', 'F', 'H'} ||
        !graph.shortest_path('H', 'A').empty() ||
        graph.shortest_path('A', 'A') != std::vector<char>{'A'}) {
        return 1;
    }
    for (char node : path) {
        std::cout << node << ' ';
    }
    std::cout << '\n';
}
