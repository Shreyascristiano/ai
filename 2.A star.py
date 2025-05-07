# Maze solver using A* Algorithm

# Define the maze grid (start at S, goal at G, # is wall, . is walkable path)
maze = [
    ['S', '.', '.', '#', '.', '.', '.', '#', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', '#', '.', '.', '#', '#', '#', '#'],
    ['#', '.', '.', '#', '.', '#', '.', '.', 'G', '#'],
    ['#', '#', '.', '#', '.', '#', '#', '.', '#', '.'],
    ['#', '.', '#', '.', '.', '.', '#', '.', '#', '#']
]

# Directions to move: right, left, down, up
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# A* Algorithm
def a_star(maze, start, goal):
    # Function to calculate Manhattan Distance (Heuristic)
    def manhattan_distance(x, y):
        return abs(x - goal[0]) + abs(y - goal[1])

    # Initialize open and closed lists
    open_list = []
    closed_list = set()

    # Start node and goal node
    start_node = (start[0], start[1], 0, manhattan_distance(start[0], start[1]), None)  # (x, y, g, h, parent)
    open_list.append(start_node)

    # Explore the maze
    while open_list:
        # Sort open list by f = g + h (cost + heuristic)
        open_list.sort(key=lambda x: x[2] + x[3])
        
        # Get the node with the lowest f value
        current = open_list.pop(0)
        x, y, g, h, parent = current

        # Mark as visited
        closed_list.add((x, y))

        # If we reached the goal, reconstruct the path
        if (x, y) == goal:
            path = []
            while parent:
                path.append((x, y))
                x, y, _, _, parent = parent
            path.reverse()
            return path

        # Expand neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != '#' and (nx, ny) not in closed_list:
                g_new = g + 1
                h_new = manhattan_distance(nx, ny)
                open_list.append((nx, ny, g_new, h_new, current))

        # Print the current maze state with visited nodes
        print_maze_with_visited(maze, closed_list)

    return None

# Function to print the maze with visited nodes
def print_maze_with_visited(maze, visited):
    for i in range(len(maze)):
        row = ""
        for j in range(len(maze[0])):
            if (i, j) in visited:
                row += 'V'  # Visited node
            else:
                row += maze[i][j]
        print(row)
    print("\n" + "="*20 + "\n")

# Main execution
start = (0, 0)  # Starting point (S)
goal = (4, 8)   # Goal point (G)

# Solve the maze using A* and print the path
path = a_star(maze, start, goal)

# Print final path
if path:
    print("Final Path from start to goal:")
    for (x, y) in path:
        maze[x][y] = '*'
    for row in maze:
        print(' '.join(row))
else:
    print("No path found.")
