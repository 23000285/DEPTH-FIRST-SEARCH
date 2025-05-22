from collections import deque
from collections import defaultdict

# BFS function
def bfs(graph, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True

    while len(queue) != 0:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if not visited[neighbour]:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

graph = defaultdict(list)

# Input number of vertices and edges
v_count, e = map(int, input("Enter number of nodes and edges: ").split())

# Input graph edges
for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

# Input starting node
start = input("Enter the start node: ")

# Initialize visited and path
visited = defaultdict(bool)
path = []

# Call BFS and print result
traversedpath = bfs(graph, start, visited, path)
print("BFS Traversal:", traversedpath)
