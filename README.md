# Maze Solving Algorithms

An implementation of maze-solving algorithms comparing Depth-First Search (DFS) and Breadth-First Search (BFS) approaches to maze pathfinding.

## Features
- Maze generation and visualization
- Multiple pathfinding implementations:
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
- Colored terminal output for maze visualization
- Path reconstruction and solution display
- Performance metrics (states explored)

## File Structure
- `DFS_Search.py` - DFS implementation
- `BFS.py` - BFS implementation
- `Maze_Generator.py` - Maze creation and handling
- `Utility.py` - Shared functions for visualization
- `Maze1.txt` - Sample maze file

## Usage

### Running DFS Algorithm:
```bash
python DFS_Search.py
```

### Running BFS Algorithm:
```bash
python BFS.py
```

Enter the maze file name when prompted (e.g., 'Maze1.txt')

## Maze Format
Mazes should be text files with the following characters:
- `#` - Wall
- `A` - Starting point
- `B` - End point (goal)
- ` ` (space) - Open path

## Algorithm Comparison
- **DFS**: Uses a stack-based approach, may not find the shortest path
- **BFS**: Uses a queue-based approach, guarantees the shortest path

## Sample Input
```
####B###
#     #
# # # #
# # # #
#A    #
#######
```

## Requirements
- Python 3.x
- No additional packages required