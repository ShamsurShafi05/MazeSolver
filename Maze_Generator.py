class MazeBlock:
    def __init__(self, elem, x = 0, y = 0):
        self.element = elem
        self.x = x
        self.y = y
        self.parent = None  # Initialize parent to None
        self.neighbors = []

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class MazeGenerator:
    def __init__(self, filename = "Maze1.txt"):
        try:
            self.MazeArray = []
            with open(filename, "r") as file:
                while True:
                    line = file.readline()
                    if not line:
                        break
                                       
                    list1 = []
                    for i in line:
                        if i == "\n":
                            break
                        if i == " ":
                            i = '@'
                        list1.append(MazeBlock(i))
                    self.MazeArray.append(list1)

            # for i in range(len(self.MazeArray)):
            #     for j in range(len(self.MazeArray[i])):
            #         print(self.MazeArray[i][j].element, end="")
            #     print()

        except FileNotFoundError:
            print("File not found. Please ensure 'maze.txt' is in the same directory.")
        
        self.start = None
        for i in range(len(self.MazeArray)):
            for j in range(len(self.MazeArray[i])):
                if self.MazeArray[i][j].element == 'A':
                    self.start = self.MazeArray[i][j]
                if i > 0:
                    self.MazeArray[i][j].add_neighbor(self.MazeArray[i-1][j])
                if i < len(self.MazeArray) - 1:
                    self.MazeArray[i][j].add_neighbor(self.MazeArray[i+1][j])
                if j > 0:
                    self.MazeArray[i][j].add_neighbor(self.MazeArray[i][j-1])
                if j < len(self.MazeArray[i]) - 1:
                    self.MazeArray[i][j].add_neighbor(self.MazeArray[i][j+1])
        

    def print_maze_grid(self):
        for i in range(len(self.MazeArray)):
            for j in range(len(self.MazeArray[i])):
                if self.MazeArray[i][j].element == '#':
                    print("\033[1;30;41m▓▓\033[0m", end="")  # Red background with black border for walls
                elif self.MazeArray[i][j].element == 'A':
                    print("\033[1;30;42mA \033[0m", end="")  # Green background with A for start
                elif self.MazeArray[i][j].element == 'B':
                    print("\033[1;30;44m B\033[0m", end="")  # Blue background with B for end
                else:
                    print("\033[1;30;47m  \033[0m", end="")  # White background with border for paths
            print()  # New line after each row

