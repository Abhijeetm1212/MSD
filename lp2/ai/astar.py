
import copy

class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, data, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(data) and y2 >= 0 and y2 < len(data):
            temp_data = copy.deepcopy(data)
            temp = temp_data[x2][y2]
            temp_data[x2][y2] = temp_data[x1][y1]
            temp_data[x1][y1] = temp
            return temp_data
        else:
            return None

    def find(self, data, x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if data[i][j] == x:
                    return i, j

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.open = []
        self.closed = []

    def accept(self):
        puz = []
        for i in range(0, self.size):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def print_board(self, state):
        for i in state:
            for j in i:
                print(j, end=" ")
            print("")

    def process(self):
        print("Enter the start state  \n")
        start = self.accept()
        print("Enter the goal state  \n")
        goal = self.accept()
        
        start_node = Node(start, 0, 0)
        start_node.fval = self.f(start_node, goal)
        self.open.append(start_node)

        print("\nStarting the puzzle solving process...\n")

        while True:
            # Pop the state with the lowest fval (A* algorithm)
            cur = self.open[0]
            
            # Print the current state of the board
            print("\nCurrent state:")
            self.print_board(cur.data)
            
            # Check if the goal state is reached
            if self.h(cur.data, goal) == 0:
                print("\nPuzzle is solved!")
                break

            # Generate children (next possible states)
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)

            # Move the current state to closed and remove it from open list
            self.closed.append(cur)
            del self.open[0]

            # Sort open list by fval (ascending order)
            self.open.sort(key=lambda x: x.fval, reverse=False)

# Create a Puzzle object with size 3 (3x3 grid)
puz = Puzzle(3)
puz.process()























































'''
import copy

# Node class represents a state in the puzzle and stores its details
class Node:
    def __init__(self, data, level, fval):
        self.data = data  # The state of the puzzle (2D grid)
        self.level = level  # The current depth level of the node (i.e., number of moves made so far)
        self.fval = fval  # The f-value (cost function: f(n) = g(n) + h(n))

    # Generate all possible child nodes by sliding the blank space ('_')
    def generate_child(self):
        x, y = self.find(self.data, '_')  # Find the position of the blank space ('_')
        
        # Possible movements for the blank space (up, down, left, right)
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        
        children = []  # List to hold the child nodes
        
        for i in val_list:
            # Try to shuffle the blank space to a new valid position
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                # Create a new node for each valid child and add to the list
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    # Swap the blank space with a valid adjacent tile
    def shuffle(self, data, x1, y1, x2, y2):
        # Check if the new position is within bounds
        if x2 >= 0 and x2 < len(data) and y2 >= 0 and y2 < len(data):
            temp_data = copy.deepcopy(data)  # Create a deep copy of the current state
            temp = temp_data[x2][y2]  # Store the tile in the new position
            temp_data[x2][y2] = temp_data[x1][y1]  # Move the blank space to the new position
            temp_data[x1][y1] = temp  # Move the tile from the new position to the blank space
            return temp_data  # Return the new state after the shuffle
        else:
            return None  # Return None if the new position is out of bounds

    # Find the position of the blank space ('_') in the grid
    def find(self, data, x):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if data[i][j] == x:  # If the tile is the blank space ('_')
                    return i, j  # Return the coordinates of the blank space

# Puzzle class represents the 8-puzzle and manages the solving process
class Puzzle:
    def __init__(self, size):
        self.size = size  # Size of the puzzle (e.g., 3 for a 3x3 puzzle)
        self.open = []  # List to store open nodes (states to be explored)
        self.closed = []  # List to store closed nodes (states already explored)

    # Accept the state input from the user (the 3x3 grid)
    def accept(self):
        puz = []
        for i in range(0, self.size):
            # Read each row and convert it into a list of integers
            temp = input().split(" ")
            puz.append(temp)
        return puz

    # Calculate the f-value (f(n) = g(n) + h(n))
    def f(self, start, goal):
        return self.h(start.data, goal) + start.level  # f(n) = h(n) + g(n)

    # Heuristic function (h(n)) calculates the number of misplaced tiles
    def h(self, start, goal):
        temp = 0
        for i in range(0, self.size):
            for j in range(0, self.size):
                # Compare the current state with the goal state
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1  # Increment for each misplaced tile
        return temp

    # Print the current state of the board
    def print_board(self, state):
        for i in state:
            for j in i:
                print(j, end=" ")  # Print each element of the row
            print("")  # Print a new line after each row

    # Main process to solve the puzzle using A* algorithm
    def process(self):
        print("Enter the start state matrix (3x3 grid) \n")
        start = self.accept()  # Accept the start state from the user
        print("Enter the goal state matrix (3x3 grid) \n")
        goal = self.accept()  # Accept the goal state from the user
        
        start_node = Node(start, 0, 0)  # Create the starting node
        start_node.fval = self.f(start_node, goal)  # Calculate the f-value for the start node
        self.open.append(start_node)  # Add the start node to the open list

        print("\nStarting the puzzle solving process...\n")

        while True:
            # Pop the state with the lowest f-value (A* algorithm)
            cur = self.open[0]
            
            # Print the current state of the board
            print("\nCurrent state:")
            self.print_board(cur.data)
            
            # Check if the goal state is reached (i.e., no misplaced tiles)
            if self.h(cur.data, goal) == 0:
                print("\nPuzzle is solved!")
                break  # Exit the loop when the puzzle is solved

            # Generate all possible child nodes (next valid states)
            for i in cur.generate_child():
                i.fval = self.f(i, goal)  # Calculate the f-value for each child node
                self.open.append(i)  # Add the child node to the open list

            # Move the current state to the closed list and remove it from the open list
            self.closed.append(cur)
            del self.open[0]

            # Sort the open list by f-value in ascending order
            self.open.sort(key=lambda x: x.fval, reverse=False)

# Create a Puzzle object with size 3 (3x3 grid) and start the solving process
puz = Puzzle(3)
puz.process()


Enter the start state  

1 2 3
4 5 6 
_ 8 9
Enter the goal state  

1 2 3
4 5 6
8 9 _
'''






