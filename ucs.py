import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

def uniform_cost_search(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node == goal:
            print("Goal Found:", node)
            print("Minimum Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbour, edge_cost in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(priority_queue,
                                   (cost + edge_cost, neighbour))

    print("Goal Not Found")

uniform_cost_search(graph, 'A', 'F')