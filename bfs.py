graph = {
  '1' : ['2','3'],
  '2' : ['2', '4'],
  '3' : ['5'],
  '4' : ['5'],
  '5' : []
}
visited = [] 
queue = []
def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  while queue:
    current_node = queue.pop(0) 
    print (current_node, end = " ") 
    for neighbour in graph[current_node]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("Breadth-First Search")
bfs(visited, graph, '1') 
