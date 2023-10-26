graph = {
    'Arad': ['Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Timisoara': ['Arad'],
    'Oradea': ['Zerind'],
}
visited = []
def dfs(start_node):
    stack = [start_node]
    while stack:
        current_city = stack.pop()
        if current_city not in visited:
            visited.append(current_city)
            print(current_city, end=" ")
        unvisited_neighbors = [city for city in graph[current_city] if city not in visited]
        stack.extend(unvisited_neighbors)
print("DFS: ")
dfs('Arad')
