# Helper: Find root of a node
def find(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node

# Helper: Union two sets
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

# Kruskal's Algorithm (Greedy MST)
def kruskal_mst(nodes, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Initially each node is its own parent (disjoint set)
    parent = {node: node for node in nodes}

    mst = []
    total_cost = 0

    print("Selected edges:")

    for u, v, weight in edges:
        if union(parent, u, v):
            mst.append((u, v, weight))
            total_cost += weight
            print(f"{u} -- {v}  (weight: {weight})")

    print("\nTotal weight of MST:", total_cost)

# Example usage
nodes = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5)
]

kruskal_mst(nodes, edges)
