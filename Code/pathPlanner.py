"""
Assignment 2: Path Planning
A* Path Planning Algorithm
Author: Adarsh Karan Kesavadas Prasanth
Student ID: 11471028
"""
# Assuming motion in 4 directions - up, down, left, right
POSSIBLE_MOVEMENTS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# A custom binary heap implementation is used to store the nodes in a priority queue like structure
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        """
        Append a value to the heap and call the _heapify_up function to 
        maintain the heap property.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Remove the root node of the heap (the smallest element) and call 
        the _heapify_down function to maintain the heap property.
        """
        if self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            value = self.heap.pop()
            self._heapify_down(0)
            return value
        else:
            return None

    def _heapify_up(self, index):
        """
        Move the value at the specified index "up" the heap to its correct position- to maintain the heap property.
        """
        # Calculate the index of the parent of the node at the specified index 
        # (index - 1) // 20 is formula to find the parent of any child i
        parent_index = (index - 1) // 2 # // - integer division (floor division)
        # If the parent exists and its value is greater than the value of the node,
        # swap them and continue heapifying up
        if parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """
        Move the value at the specified index "down" the heap to its correct position- to maintain the heap property.
        """
        # Assume the node at the specified index is the smallest
        smallest = index
        # Calculate the indices of the left and right children of the node
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        # If the left child exists and its value is less than the value of the smallest node,
        # update the smallest node
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        # If the right child exists and its value is less than the value of the smallest node,
        # update the smallest node
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        # If the smallest node is not the node at the specified index, swap them and continue heapifying down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# This class represents each node- cell in a grid
class Node:
    def __init__(self, position, cost_from_start, heuristic, parent=None):
        """
        Initialize a new node with the specified position, cost from the start, heuristic cost to the goal,
        and parent node. The total cost (f) is the sum of the cost from the start and the heuristic cost.
        """
        self.position = position # x, y position of the node (col, row format)
        self.g = cost_from_start # g(n)- cost from start to node n
        self.h = heuristic # h(n)- heuristic cost from node n to goal- Euclidean distance
        self.parent = parent # parent "node" of the current node- used to retrace the path
        self.f = self.g + self.h # total cost is f(n) = g(n) + h(n)
        
    def __lt__(self, other):
        """
        A Special method to define the less than operator for nodes. So, whenever the nodes are compared in the BinaryHeap class,
        the following expression ensures that the nodes are compared based on their total cost f(n)

        This is in accordance to the main criteria of the A* algorithm where the nodes are expanded 
        based on their total cost f(n) = g(n) + h(n).
        Nodes with a lower total cost are considered less than nodes with a higher total cost.
        """
        return (self.f) < (other.f)

def euclidean_distance(current, goal):
    """
    Calculate the Euclidean distance between the current position and the goal position.
    Just returns the value without storing it in a variable- to save memory.
    """
    return ((goal[0] - current[0])**2 + (goal[1] - current[1])**2)**0.5

def is_valid_and_not_obstacle(neighbor_position, grid, COL, ROW):
    """
    Check if a cell is valid (within the grid) and is not an obstacle.
    Here 0 - obstacle, 1 - free cell
    Combined into one function- to reduce the number of function calls.
    """
    x, y = neighbor_position
    if 0 <= x < COL and 0 <= y < ROW:
        return grid[x][y]
    return False

def reconstruct_path(node, path):
    """
    Efficiently reconstructs the path from the start to the goal by following the parent pointers.
    """
    # Start with the goal node
    current = node
    # While the current node has a parent
    while current is not None:
        # Add the position of the current node to the path list
        path.append(current.position)
        # Set the current node to its parent
        current = current.parent
    # Reverse the path to get it from start to goal
    path.reverse()
    return path

# The main path planning function. Additional functions, classes, 
# variables, libraries, etc. can be added to the file, but this
# function must always be defined with these arguments and must 
# return an array ('list') of coordinates (col,row).
#DO NOT EDIT THIS FUNCTION DECLARATION
def do_a_star(grid, start, end, display_message):
    display_message("A* Path Planning Algorithm")

    # First check if there is a valid start and end point
    if not start or not end:
        display_message("No valid start or end point.")
        return [] 
    
    # Get the size of the grid
    COL = len(grid)
    ROW = len(grid[0])
    """
    open_dict: A dictionary to store the position of node as key and cost g(h) as value
                (this is to keep track of the nodes that have been visited and their cost from the start)
    closed_set: A set to store the position of nodes that have been visited and expanded.
    priority_queue: An instance of BinaryHeap Class to store the nodes in a priority queue like structure
                    to make the node with the lowest total cost (f) the root of the heap- "highest priority"
    path: A list to store the final path from the start to the goal
    """
    open_dict = {}
    closed_set = set()
    priority_queue = BinaryHeap()
    path = []
    # Pass the start node to the priority queue with g=0 and h=Euclidean distance to the goal
    priority_queue.push(Node(start, 0, euclidean_distance(start, end)))
    open_dict[start] = 0
    
    # Until the priority queue is not empty
    while priority_queue.heap:
        # Pop the node with the lowest total cost (f) from the priority queue
        current_node = priority_queue.pop()
        current_pos = current_node.position

        # If the current node is the goal node, reconstruct the path and return it
        if current_pos == end:
            path = reconstruct_path(current_node, path)
            return path
        
        # If the current node has already been visited, skip it
        if current_pos in closed_set:
            continue
        # Remove the current node from the open_dict
        del open_dict[current_pos]
        # Mark the current node as visited by adding it to the closed set
        closed_set.add(current_pos)
                
        for i in POSSIBLE_MOVEMENTS:
            x, y = current_pos
            dx, dy = i
            # Calculate the position of the neighbor
            neighbor_position = (x + dx, y + dy)
            # If neighbor is within grid(valid) and not an obstacle
            if is_valid_and_not_obstacle(neighbor_position, grid, COL, ROW):
                # Increment the cost from the start to the neighbor node by 1
                g_score = current_node.g + 1 # g
                if neighbor_position not in closed_set or (neighbor_position in open_dict and g_score < open_dict[neighbor_position]):
                    '''
                    The first condition checks if the neighbor has already been visited and expanded.
                    The second condition checks if the neighbor is in the open_dict 
                        and the new cost g(h) from the start to the neighbor is less than the old cost.
                    (This is to update the cost of the neighbor if a better path is found)
                    '''
                    heuristic = euclidean_distance(neighbor_position, end) # h(n)

                    # Add the valid neighbor to the priority queue with current node as parent, and to open_dict
                    priority_queue.push(Node(neighbor_position, g_score, heuristic, current_node))
                    open_dict[neighbor_position] = g_score

    # If the function hasn't returned yet and the priority_queue is empty, 
    # it means that all possible paths have been explored and no valid path to the end has been found.
    if len(priority_queue.heap) == 0:
        display_message("No valid path to the end found.")
        path = []
        return path

