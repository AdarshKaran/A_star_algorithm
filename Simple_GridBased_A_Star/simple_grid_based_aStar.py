from simple_binary_heap import BinaryHeap
from simple_node import Node


def euclidean_distance(current, goal):
    """The heuristic function for A* algorithm"""
    return ((goal[0] - current[0])**2 + (goal[1] - current[1])**2)**0.5


def is_valid(neighbor_position, num_cols, num_rows):
    """Check if a cell is valid (within the grid)"""
    x, y = neighbor_position
    return x in range(num_rows) and y in range(num_cols)


def is_not_obstacle(neighbor_position, grid):
    """Check if a cell is not an obstacle"""
    return grid[neighbor_position[0]][neighbor_position[1]]


def reconstruct_path(node, path):
    """Reconstruct the path from the start to the end"""
    current = node
    while current is not None:
        path.append((current.position))
        current = current.parent
    # return the path in the correct order
    return path[::-1]


def do_a_star(grid, start, end):
    """
    Perform the A* search algorithm to find the shortest path from start to end in a grid.

    Parameters:
    grid (list of list of bool): The grid to perform the search on. Each cell in the grid is a boolean indicating whether the cell is an obstacle (True means it's not an obstacle and False means it's an obstacle).
    start (tuple): The starting position in the grid. It's a tuple of two integers representing the row and column index of the starting position.
    end (tuple): The ending position in the grid. It's a tuple of two integers representing the row and column index of the ending position.

    Returns:
    list of tuple: The shortest path from start to end. Each tuple in the list represents a cell in the path, with the first element being the row index and the second element being the column index. If no valid path is found, an empty list is returned.
    """
    # assuming motion in 4 directions - up, down, left, right
    possible_movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Get the size of the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # assuming start and end are in (rows, cols) format
    if not start or not end or not grid:
        raise ValueError("Start and end positions must be defined")

    # condition for checking if start and end are within the grid
    if not is_valid(start, num_cols, num_rows) or not is_valid(end, num_cols, num_rows):
        raise ValueError("Start and end positions must be within the grid")

    # boolean grid to keep track of visited cells
    visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

    path = []
    priority_queue = BinaryHeap()
    priority_queue.push(Node(start, 0, euclidean_distance(start, end)))

    # while the priority_queue is not empty
    while priority_queue.heap:
        current_node = priority_queue.pop()
        current_pos = current_node.position
        # if the current position has been visited, skip it
        if visited[current_pos[0]][current_pos[1]]:
            continue
        # set the current position as visited
        visited[current_pos[0]][current_pos[1]] = True

        # if the current position is the end position, reconstruct the path
        if current_pos == end:
            path = reconstruct_path(current_node, path)
            return path
        # check the neighbors of the current position
        for i in possible_movement:
            x, y = current_pos
            dx, dy = i
            neighbor_position = (x + dx, y + dy)
            # if neighbor is within grid and not an obstacle and not visited
            if is_valid(neighbor_position, num_rows, num_cols) and is_not_obstacle(neighbor_position, grid):
                if not visited[neighbor_position[0]][neighbor_position[1]]:
                    cost_from_start = current_node.g + 1
                    priority_queue.push(Node(neighbor_position, 
                                             cost_from_start, 
                                             euclidean_distance(neighbor_position, end),
                                             current_node))

    # If the function hasn't returned yet and the priority_queue is empty,
    # it means that all possible paths have been explored and no valid path to the end has been found.
    if len(priority_queue.heap) == 0:
        print("No valid path to the end found")
        path = []
        return path