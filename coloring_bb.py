def is_valid(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment

    unassigned = [node for node in graph if node not in assignment]
    node = unassigned[0]

    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[node]

    return None

def graph_coloring_min_colors(graph, all_colors):
    n = len(graph)
    for k in range(1, len(all_colors) + 1):
        selected_colors = all_colors[:k]
        assignment = {}
        result = backtrack(assignment, graph, selected_colors)
        if result:
            print(f"\n✅ Minimum colors needed: {k}")
            return result
    return None

def get_user_input():
    n = int(input("Enter number of nodes: "))
    graph = {}

    print("Enter node names:")
    nodes = [input(f"Node {i+1}: ") for i in range(n)]

    for node in nodes:
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node] = neighbors

    m = int(input("Enter total colors available: "))
    colors = [input(f"Color {i+1}: ") for i in range(m)]

    return graph, colors

if __name__ == "__main__":
    graph, colors = get_user_input()
    solution = graph_coloring_min_colors(graph, colors)

    if solution:
        print("\n🎨 Color Assignment:")
        for node in solution:
            print(f"{node}: {solution[node]}")
    else:
        print("\n❌ No valid coloring found.")
