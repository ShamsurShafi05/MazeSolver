def reconstruct_path(end_node):
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = current.parent
    return path[::-1]  # Reverse path to get start->end order

def print_maze_with_path(maze, path):
    # Convert path nodes to set for O(1) lookup
    path_set = set(path)
    
    for i in range(len(maze.MazeArray)):
        for j in range(len(maze.MazeArray[i])):
            current = maze.MazeArray[i][j]
            if current in path_set:
                if current.element == 'A':
                    print("\033[1;30;43mA \033[0m", end="")  # Green A
                elif current.element == 'B':
                    print("\033[1;30;43mB \033[0m", end="")  # Blue B
                else:
                    print("\033[1;30;43m  \033[0m", end="")  # Yellow path
            else:
                if current.element == '#':
                    print("\033[1;30;41m▓▓\033[0m", end="")  # Red walls
                else:
                    print("\033[1;30;47m  \033[0m", end="")  # White space
        print()


