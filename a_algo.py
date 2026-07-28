import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

def a_star(graph, start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start))

    visited = set()

    while pq:
        f, g, node = heapq.heappop(pq)

        if node == goal:
            print("Goal Found:", node)
            print("Minimum Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(pq, (new_f, new_g, neighbour))

    print("Goal Not Found")

a_star(graph, 'A', 'G')