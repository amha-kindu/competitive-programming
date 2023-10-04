#include <iostream>
#include <vector>

const int INF = 30000;

int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<int>> edge_list;
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        std::cin >> u >> v >> w;
        edge_list.push_back({u, v, w});
    }

    std::vector<int> dist(n, INF);
    dist[0] = 0;

    for (int i = 0; i < n - 1; ++i) {
        for (const auto& edge : edge_list) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            if (dist[u - 1] != INF && dist[u - 1] + w < dist[v - 1]) {
                dist[v - 1] = dist[u - 1] + w;
            }
        }
    }

    for (int d : dist) {
        std::cout << d << " ";
    }

    return 0;
}
