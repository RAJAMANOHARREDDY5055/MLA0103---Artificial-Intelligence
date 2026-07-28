from queue import PriorityQueue

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 0,
    'E': 3,
    'F': 1
}

def greedy_best_first(start, goal):

    pq = PriorityQueue()

    pq.put((heuristic[start], start))

    visited = set()

    while not pq.empty():

        h, node = pq.get()

        if node == goal:
            print("Goal Found:", node)
            return

        visited.add(node)

        print(node, end=" ")

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                pq.put((heuristic[neighbour], neighbour))

greedy_best_first('A', 'D')