def build_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    print("Enter edges (u v) one per line:")
    for _ in range(e):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # because it's an undirected graph
    return graph

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# Driver code
graph = build_graph()
start_node = input("Enter starting node: ")

print("\nDFS Traversal:")
dfs(graph, start_node, set())

print("\nBFS Traversal:")
bfs(graph, start_node)
