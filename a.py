import queue
graph = {
    'Arad': {'Zerind': 75, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118},
    'Oradea': {'Zerind': 71}
}
heuristic = {
    'Arad': 170, 'Zerind': 71, 'Timisoara': 329, 'Oradea': 380
}
def astar_search(graph, start, goal, heuristic):
    q = queue.PriorityQueue()
    q.put((0, start))
    came_from, g_score = {}, {city: float('inf') for city in graph}
    g_score[start] = 0
    while not q.empty():
        _, current = q.get()
        if current == goal:
            path, current = [], goal
            while current:
                path.insert(0, current)
                current = came_from.get(current)
            return path
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                q.put((f_score, neighbor))
print("A* Path:", astar_search(graph, 'Arad', 'Oradea', heuristic))
