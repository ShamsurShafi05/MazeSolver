from Maze_Generator import MazeGenerator
from Utility_Functions import print_maze_with_path, reconstruct_path
import random

class StackFrontier:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    
class DFS:
    def __init__(self, maze):
        self.maze = maze
        self.frontier = StackFrontier()
        self.explored = set()
        self.explored_states = 0

    def search(self):
        self.frontier.push(self.maze.start)

        while not self.frontier.is_empty():
            current_node = self.frontier.pop()
            self.explored_states += 1

            if current_node.element == 'B':
                return reconstruct_path(current_node)

            self.explored.add(current_node)

            # Randomize neighbors before adding to frontier (to demonsatrate DFS sometimes shows suboptimal path)
            neighbors = list(current_node.neighbors)
            random.shuffle(neighbors)

            for neighbor in neighbors:
                if neighbor not in self.explored and neighbor not in self.frontier.stack and neighbor.element != '#':
                    neighbor.parent = current_node  # Set parent for path reconstruction
                    self.frontier.push(neighbor)

        return None  # No path found
    
file = input("Enter the maze file name (eg. 'Maze1.txt'): ")
maze = MazeGenerator(file)
dfs = DFS(maze)
path = dfs.search()
if path:
    print("Path found using DFS:")
    print_maze_with_path(maze, path)
    print("Number of explored states:", dfs.explored_states)
else:   
    print("No path found using DFS.")
    print("Number of explored states:", dfs.explored_states)
