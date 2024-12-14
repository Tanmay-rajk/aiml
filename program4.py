from collections import deque
def bfs(graph, start):
visited = set()
queue = deque([start])
paths = {start: [start]}
while queue:
vertex = queue.popleft()
if vertex not in visited:
visited.add(vertex)
print(f"visited: {vertex}, path: {paths[vertex]}")
for neighbor in graph[vertex]:
if neighbor not in visited:
queue.append(neighbor)
paths[neighbor] = paths[vertex] + [neighbor]
return paths
graph = {
'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B'],
'E': ['B', 'F'],
'F': ['C', 'E']
}
print("bfs starting from A")
start_node = 'A'
paths = bfs(graph, start_node)
