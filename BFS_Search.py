from Maze_Generator import MazeGenerator
from Utility import print_maze_with_path, reconstruct_path
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.frontier = Queue()
        self.explored = set()
        self.explored_states = 0

    def search(self):
        self.frontier.enqueue(self.maze.start)

        while not self.frontier.is_empty():
            current_node = self.frontier.dequeue()
            self.explored_states += 1

            if current_node.element == 'B':
                return reconstruct_path(current_node)

            self.explored.add(current_node)
            
            # Randomize neighbors before adding to frontier (to demonsatrate DFS sometimes shows suboptimal path)
            neighbors = list(current_node.neighbors)
            random.shuffle(neighbors)

            for neighbor in neighbors:
                if neighbor not in self.explored and neighbor not in self.frontier.items and neighbor.element != '#':
                    neighbor.parent = current_node  # Set parent for path reconstruction
                    self.frontier.enqueue(neighbor)

        return None  # No path found
    
file = input("Enter the maze file name (eg. 'Maze1.txt'): ")
maze = MazeGenerator(file)
bfs = BFS(maze)
path = bfs.search()
if path:
    print("Path found using BFS:")
    print_maze_with_path(maze, path)
    print("Number of explored states:", bfs.explored_states)
else:
    print("No path found using BFS.")
    print("Number of explored states:", bfs.explored_states)