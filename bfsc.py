graph = {
    'Arad': ['Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad'],
    'Oradea': ['Zerind'],
}
visited = []
def bfs(start_node):
    queue = [start_node]
    visited.append(start_node)
    while queue:
        current_city = queue.pop(0)
        print(current_city, end=" ")
        for city in graph[current_city]:
            if city not in visited:
                visited.append(city)
                queue.append(city)
print("Breadth-First Search:")
bfs('Arad')
